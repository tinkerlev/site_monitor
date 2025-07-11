# 🔍 Site Availability Monitor

A lightweight Python script that monitors website uptime and sends **email alerts** on downtime or recovery events.
Designed for websites hosted on **WordPress** and protected by **Cloudflare**, with full logging support.

---
<div align="center">

<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/SMTP-Email-ff69b4?style=for-the-badge" />
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" />
<img src="https://img.shields.io/badge/Windows-Task_Scheduler-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Requests-HTTP_Client-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/Logging-Built_in-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Dotenv-Config-green?style=for-the-badge" />

</div>


## 📦 Features

* ⏱️ Periodic health checks (configurable interval)
* 📬 Email alerts via Gmail SMTP (App Password support)
* 👢 Log file with timestamped events
* ♻️ Auto-recovery detection (notifies when site comes back online)
* 🛡️ Works behind Cloudflare / CDN / Reverse Proxies

---

## 🛠️ Requirements

* Python 3.6+
* Internet access (for outbound HTTP and SMTP)
* Gmail account with **App Password**

### 🔪 Python dependencies:

Install using pip:

```bash
pip install -r requirements.txt
```

> `requirements.txt` contains:

```
requests==2.31.0
```

---

## 🚀 Installation

### 1. Clone the repo:

```bash
git clone https://github.com/YOUR_USERNAME/site-monitor.git
cd site-monitor
```

### 2. Edit your config in `site_monitor.py`:

```python
SITE_URL = "https://yourdomain.com"
EMAIL_FROM = "your_alert_email@gmail.com"
EMAIL_TO = "your_email@gmail.com"
SMTP_USER = "your_alert_email@gmail.com"
SMTP_PASS = "your_app_password"
```

### 3. Run the script:

```bash
python site_monitor.py
```

---

## 👤 Auto-run on Windows (Optional)

1. Open **Task Scheduler**
2. Create a new task with:

   * **Trigger:** At system startup
   * **Action:** Start program → `python.exe`
   * **Arguments:** `"C:\Path\To\site_monitor.py"`

✅ Enable **"Run whether user is logged in or not"** and **"Run with highest privileges"**

---

## 📁 File Structure

```
site-monitor/
├── site_monitor.py         # Main script
├── requirements.txt        # Dependencies
└── README.md               # This file
```

---

## 📓 Sample Output (uptime.log)

```
[2025-07-11 09:32:17] === Script started ===
[2025-07-11 09:35:10] DOWN - Status: 503
[2025-07-11 09:37:45] UP AGAIN - Status: 200
```

---

## 🔐 Security Tips

* Do not commit `SMTP_PASS` to public repositories.
* Use `.env` files or environment variables for sensitive data.
* Enable 2FA on your Gmail account and use **App Passwords** only.

---

## 📬 Want Telegram or Discord alerts instead of email?

Let me know – the script is modular and can easily support webhooks, Telegram bots, or Slack integrations.

---

## 👨‍💻 Created By

Eliran Loai Deeb – [LinkedIn](https://www.linkedin.com/in/loai-deeb/)
Ethical Hacker & Cybersecurity Professional | AI-Security | WordPress Security | PTES, OWASP, NIST 800-115
