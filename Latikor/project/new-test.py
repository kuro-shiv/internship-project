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
# Function: UI Login
# ---------------------
def login(email, password):
    print(f"\n[INFO] Attempting login")
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
        response = requests.post(url, json={"EmailId": EMAIL, "Password": PASSWORD})
        print("[DEBUG] Login API response Saved")

        if response.status_code == 200:
            json_data = response.json()
            token = json_data.get("result", [{}])[0].get("token")
            if token:
                print("[INFO] Token retrieved.")
                return token
            else:
                print("[ERROR] Token not found in response.")
        else:
            print(f"[ERROR] Login API returned {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Failed to get token: {e}")
    return None


# ---------------------
# Function: Validate API
# ---------------------
def validate_api(api_number, url, method="GET", data=None, expected_status=200, headers=None):
    time.sleep(2)
    try:
        response = requests.post(url, json=data, headers=headers) if method == "POST" else requests.get(url, headers=headers)
        status = response.status_code
        result = "✅ PASS" if status == expected_status else f"❌ FAIL (Expected: {expected_status})"
        print(f"[API {api_number}] Status Code: {status} — {result}")
    except Exception as e:
        print(f"[API {api_number}] ❌ Exception during API call: {e}")

# ---------------------
# Function: Send Email Report
# ---------------------
def send_login_email(success, reason):
    if not all([GMAIL_SENDER, GMAIL_APP_PASS, REPORT_RECEIVER]):
        print("[ERROR] Missing email credentials in .env file.")
        return

    subject = "✅ Login Success Report" if success else "❌ Login Failed Alert"
    body = "Login was successful!" if success else f"Login failed.\nReason: {reason}"

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
token = get_auth_token()
auth_headers = {"Authorization": f"Bearer {token}"} if token else {}

# API 2: Role Permission
validate_api(
    api_number=2,
    url="https://blue.api.s10drd.com/User/api/RolePermission/GetRolePermissionByRoleId?roleId=2&userId=1",
    headers=auth_headers,
    expected_status=200
)

# API 3: Insufficient Product
validate_api(
    api_number=3,
    url="https://blue.api.s10drd.com/Ordering/api/Order/GetInsufficientProduct?UserId=1&PageSize=20&sort=desc",
    headers=auth_headers,
    expected_status=200
)

# UI Login + Email Report
login_success, reason = login(EMAIL, PASSWORD)
send_login_email(login_success, reason)

# Cleanup
time.sleep(2)
driver.quit()
print("[INFO] Script finished.")

