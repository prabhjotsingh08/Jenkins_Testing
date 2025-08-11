# backend/app/notifications.py
import smtplib
from email.message import EmailMessage
import requests
from .config import settings
from typing import Dict

def send_email(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = f"{settings.APP_NAME} <ci@example.com>"
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)
    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as s:
        s.send_message(msg)

def send_slack_message(text: str):
    if not settings.SLACK_WEBHOOK_URL:
        print("No Slack webhook configured, skipping.")
        return
    payload = {"text": text}
    resp = requests.post(settings.SLACK_WEBHOOK_URL, json=payload)
    resp.raise_for_status()

def notify_build_result(job, result: Dict):
    subject = f"[{result.get('status')}] Build for job {job.name}"
    body = f"Result: {result}\n"
    # For demo: send email to maintainer@example.com
    try:
        send_email("maintainer@example.com", subject, body)
    except Exception as e:
        print("Email notification failed:", e)
    try:
        send_slack_message(subject + "\n" + str(result))
    except Exception as e:
        print("Slack notification failed:", e)
