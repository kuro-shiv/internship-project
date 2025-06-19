import os
import time
import requests
import smtplib
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------
# Load environment variables
# ---------------------
load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
LOGIN_URL = os.getenv("LOGIN_URL")
GMAIL_SENDER = os.getenv("GMAIL_SENDER")
GMAIL_APP_PASS = os.getenv("GMAIL_APP_PASS")
REPORT_RECEIVER = os.getenv("REPORT_RECEIVER")



# ---------------------
# Headless environment variables
# ---------------------
headless = os.getenv("HEADLESS", "False").lower() == "true"

# Configure Chrome options
options = Options()
if headless:
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

# Initialize driver once
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(LOGIN_URL)






# ---------------------
# Function: UI Login
# ---------------------
def login(email, password):
    print(f"\n[INFO] Attempting UI login")
    driver.get(LOGIN_URL)
    time.sleep(2)

    try:
        driver.find_element(By.ID, "EmailId").clear()
        driver.find_element(By.ID, "Password").clear()
        time.sleep(1)

        print("[INFO] Entering credentials...")
        driver.find_element(By.ID, "EmailId").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "Password").send_keys(Keys.RETURN)

        time.sleep(6)
        driver.find_element(By.XPATH, "//h2[normalize-space()='Dashboard']")
        print("[SUCCESS] UI Login successful ✅")
        return True, None

    except NoSuchElementException:
        error_msg = "Dashboard not found. Possibly invalid credentials."
        print(f"[FAIL] Login failed ❌ — {error_msg}")
        return False, error_msg

    except Exception as e:
        print(f"[ERROR] Unexpected failure: {e}")
        return False, str(e)


# ---------------------
# Function: Get Auth Token
# ---------------------
def get_auth_token():
    url = "https://blue.api.s10drd.com/authentication/api/login/signin"
    try:
        print("[INFO] Attempting API login to get token")
        response = requests.post(url, json={"EmailId": EMAIL, "Password": PASSWORD})

        if response.status_code == 200:
            json_data = response.json()
            token = json_data.get("result", [{}])[0].get("token")
            if token:
                print("[SUCCESS] Token retrieved ✅")
                return token
            else:
                print("[ERROR] Token not found in response")
        else:
            print(f"[ERROR] Login API returned {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed to get token: {e}")
    return None


# ---------------------
# Function: Validate API
# ---------------------
def validate_api(api_number, url, method="GET", data=None, expected_status=200, headers=None):
    print(f"\n[API {api_number}] Testing: {url}")
    time.sleep(2)
    try:
        if method == "POST":
            response = requests.post(url, json=data, headers=headers)
        else:
            response = requests.get(url, headers=headers)

        status = response.status_code
        result = "✅ PASS" if status == expected_status else f"❌ FAIL (Expected: {expected_status})"
        print(f"[API {api_number}] Status Code: {status} — {result}")
        print(f"[API {api_number}] Response: {response.text[:200]}...")  # Print first 200 chars

        return status == expected_status
    except Exception as e:
        print(f"[API {api_number}] ❌ Exception during API call: {e}")
        return False


# ---------------------
# Function: Count Images and Save Data
# ---------------------
def process_customer_records():
    print("\n[INFO] Starting customer records processing")
    try:
        # Navigate to Estimating Customer Info
        driver.find_element(By.XPATH, "//i[2]//*[name()='svg']").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Estimating Customer Info')]").click()
        time.sleep(3)

        # Get all customer rows
        rows = driver.find_elements(By.XPATH, "//tbody/tr")
        print(f"[INFO] Found {len(rows)} customer records to process")

        results = []

        for i in range(1, len(rows) + 1):
            try:
                # Click on customer
                xpath = f"//tbody/tr[{i}]/td[2]"
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(2)

                # Count images
                images = driver.find_elements(By.TAG_NAME, "img")
                image_count = len([img for img in images if img.is_displayed()])
                print(f"[RECORD {i}] Found {image_count} displayed images")

                # Get property name
                try:
                    property_name = driver.find_element(By.XPATH, "//label[@for='shipToPropertyName']").text
                except NoSuchElementException:
                    property_name = "Not found"

                results.append({
                    "record": i,
                    "property_name": property_name,
                    "image_count": image_count
                })

                # Go back to list
                driver.back()
                time.sleep(2)

            except Exception as e:
                print(f"[ERROR] Failed to process record {i}: {str(e)}")
                continue

        print("\n[INFO] Processing results:")
        for result in results:
            print(f"Record {result['record']}: {result['property_name']} - {result['image_count']} images")

        return results

    except Exception as e:
        print(f"[ERROR] Failed to process customer records: {e}")
        return []


# ---------------------
# Function: Send Email Report
# ---------------------
def send_login_email(success, reason, api_results=None, customer_data=None):
    if not all([GMAIL_SENDER, GMAIL_APP_PASS, REPORT_RECEIVER]):
        print("[ERROR] Missing email credentials in .env file.")
        return

    subject = "✅ Automation Report: Success" if success else "❌ Automation Report: Failed"
    msg = MIMEMultipart()
    msg["From"] = GMAIL_SENDER
    msg["To"] = REPORT_RECEIVER
    msg["Subject"] = subject

    body = "Automation Test Results\n\n"
    body += "Login Status: " + ("Success ✅\n" if success else f"Failed ❌\nReason: {reason}\n")

    if api_results:
        body += "\nAPI Test Results:\n"
        body += "----------------\n"
        for i, result in enumerate(api_results, 1):
            status = "PASS ✅" if result else "FAIL ❌"
            body += f"API {i}: {status}\n"

    if customer_data:
        body += "\nCustomer Data Processing:\n"
        body += "------------------------\n"
        body += f"Processed {len(customer_data)} records\n"
        for item in customer_data:
            body += f"Record {item['record']}: {item['property_name']} - {item['image_count']} images\n"

    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(GMAIL_SENDER, GMAIL_APP_PASS)
        server.sendmail(GMAIL_SENDER, REPORT_RECEIVER, msg.as_string())
        server.quit()
        print("[INFO] Report email sent.")
    except Exception as e:
        print(f"[ERROR] Could not send email: {e}")


# ---------------------
# Main Execution
# ---------------------
def main():
    # API Authentication
    token = get_auth_token()
    auth_headers = {"Authorization": f"Bearer {token}"} if token else {}

    # API Tests
    api_results = []
    api_results.append(validate_api(
        api_number=1,
        url="https://blue.api.s10drd.com/authentication/api/login/signin",
        method="POST",
        data={"EmailId": EMAIL, "Password": PASSWORD},
        expected_status=200
    ))

    api_results.append(validate_api(
        api_number=2,
        url="https://blue.api.s10drd.com/User/api/RolePermission/GetRolePermissionByRoleId?roleId=2&userId=1",
        headers=auth_headers,
        expected_status=200
    ))

    api_results.append(validate_api(
        api_number=3,
        url="https://blue.api.s10drd.com/Ordering/api/Order/GetInsufficientProduct?UserId=1&PageSize=20&sort=desc",
        headers=auth_headers,
        expected_status=200
    ))

    # UI Login
    login_success, reason = login(EMAIL, PASSWORD)

    # Process customer data if UI login successful
    customer_data = []
    if login_success:
        customer_data = process_customer_records()

    # Send comprehensive report
    send_login_email(login_success, reason, api_results, customer_data)

    # Cleanup
    time.sleep(2)
    driver.quit()
    print("[INFO] Script finished.")


if __name__ == "__main__":
    main()