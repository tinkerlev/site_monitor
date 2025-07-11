from dotenv import load_dotenv
import os
import requests
import time
from datetime import datetime
import smtplib
from email.message import EmailMessage

# === Configuration ===
SITE_URL = "https://www.example.com"
CHECK_INTERVAL = 60
LOG_FILE = "uptime.log"

load_dotenv()
# Email configuration
SITE_URL = os.getenv("SITE_URL")
CHECK_INTERVAL = int(os.getenv("CHECK_INTERVAL", 60))
EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_SUBJECT = "⚠️ Site Down Alert"
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")

required_vars = [SITE_URL, EMAIL_FROM, EMAIL_TO, SMTP_USER, SMTP_PASS]
if not all(required_vars):
    raise EnvironmentError("[!] One or more required environment variables are missing. Check your .env file.")

def send_email_alert(message: str) -> None:
    """Send an email alert with the provided message."""
    msg = EmailMessage()
    msg.set_content(f"{message}\nTimestamp: {datetime.now()}")
    msg["Subject"] = EMAIL_SUBJECT
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
    except Exception as e:
        print(f"[!] Email sending failed: {e}")

def log_event(entry: str) -> None:
    """Append an entry to the log file with a timestamp."""
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{datetime.now()}] {entry}\n")

def monitor_site() -> None:
    """Continuously monitor the site and log status changes."""
    log_event("=== Monitor script started ===")
    print(f"[+] Monitoring {SITE_URL} every {CHECK_INTERVAL} seconds...")
    was_down = False

    while True:
        try:
            response = requests.get(SITE_URL, timeout=10)
            status = response.status_code

            if status != 200:
                log_event(f"DOWN - HTTP {status}")
                if not was_down:
                    send_email_alert(f"Site DOWN (HTTP {status})")
                    was_down = True
            else:
                if was_down:
                    log_event(f"RECOVERED - HTTP {status}")
                    send_email_alert("Site is back ONLINE")
                    was_down = False

        except requests.RequestException as e:
            log_event(f"ERROR - {e}")
            if not was_down:
                send_email_alert(f"Site ERROR - {e}")
                was_down = True

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_site()
