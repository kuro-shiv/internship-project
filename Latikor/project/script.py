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
# Setup Chrome Browser
# ---------------------
options = Options()
driver = webdriver.Chrome(options=options)
driver.maximize_window()


# ---------------------
# Function: Login
# ---------------------
def login(email, password):
    print(f"\n[INFO] Attempting login with: {email}")
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
        print("[SUCCESS] Login successful ✅")

        # Get cookies from Selenium and convert to requests format
        selenium_cookies = driver.get_cookies()
        cookies = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
        print(f"[DEBUG] Cookies captured: {cookies.keys()}")
        return True, None, cookies

    except NoSuchElementException:
        error_msg = "Dashboard not found. Possibly invalid credentials."
        print(f"[FAIL] Login failed ❌ — {error_msg}")
        return False, error_msg, None

    except Exception as e:
        print(f"[ERROR] Unexpected failure: {e}")
        return False, str(e), None


# ---------------------
# Function: API Validation with detailed logging
# ---------------------
def validate_api(api_number, url, method="GET", data=None, expected_status=200, cookies=None, headers=None):
    print(f"\n[API {api_number}] Testing: {url}")
    print(f"[API {api_number}] Method: {method}")
    print(f"[API {api_number}] Params/Data: {data}")

    time.sleep(2)
    try:
        if method == "POST":
            response = requests.post(url, json=data, cookies=cookies, headers=headers)
        else:
            response = requests.get(url, params=data, cookies=cookies, headers=headers)

        status = response.status_code
        result = "✅ PASS" if status == expected_status else f"❌ FAIL (Expected: {expected_status})"

        # Detailed logging
        print(f"[API {api_number}] Status Code: {status} — {result}")
        print(f"[API {api_number}] Response Headers: {response.headers}")
        print(f"[API {api_number}] Response Content (first 200 chars): {response.text[:200]}")

        # If response is JSON, print it prettily
        try:
            json_response = response.json()
            print(f"[API {api_number}] JSON Response: {json_response}")
        except ValueError:
            pass

        return status == expected_status

    except Exception as e:
        print(f"[API {api_number}] ❌ Exception during API call: {str(e)}")
        return False


# ---------------------
# Function: Email Report
# ---------------------
def send_login_email(success, reason, api_results=None):
    if not all([GMAIL_SENDER, GMAIL_APP_PASS, REPORT_RECEIVER]):
        print("[ERROR] Missing email credentials in .env file.")
        return

    subject = "✅ Login Success Report" if success else "❌ Login Failed Alert"
    body = "Login was successful!\n\n" if success else f"Login failed.\nReason: {reason}\n\n"

    if api_results:
        body += "API Validation Results:\n"
        body += "----------------------\n"
        for i, result in enumerate(api_results, 1):
            status = "PASS" if result else "FAIL"
            body += f"API {i}: {status}\n"

    msg = MIMEMultipart()
    msg["From"] = GMAIL_SENDER
    msg["To"] = REPORT_RECEIVER
    msg["Subject"] = subject
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
# First login to get session cookies
login_success, reason, cookies = login(EMAIL, PASSWORD)

api_results = []
if login_success and cookies:
    # Define common headers
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Test APIs with the obtained cookies
    print("\n[INFO] Starting API tests with session cookies...")

    # API 1: Sign In API
    api1_success = validate_api(
        api_number=1,
        url="https://blue.api.s10drd.com/authentication/api/login/signin",
        method="POST",
        data={"EmailId": EMAIL, "Password": PASSWORD},
        expected_status=200
    )
    api_results.append(api1_success)

    # API 2: Role Permissions API
    api2_success = validate_api(
        api_number=2,
        url="https://blue.api.s10drd.com/User/api/RolePermission/GetRolePermissionByRoleId",
        method="GET",
        data={"roleId": "2", "userId": "2"},
        expected_status=200,
        cookies=cookies,
        headers=headers
    )
    api_results.append(api2_success)

    # API 3: Insufficient Products API
    api3_success = validate_api(
        api_number=3,
        url="https://blue.api.s10drd.com/Ordering/api/Order/GetInsufficientProduct",
        method="GET",
        data={"UserId": "1", "PageSize": "20", "sort": "desc"},
        expected_status=200,
        cookies=cookies,
        headers=headers
    )
    api_results.append(api3_success)

send_login_email(login_success, reason, api_results if login_success else None)

time.sleep(2)
driver.quit()
print("[INFO] Script finished.")