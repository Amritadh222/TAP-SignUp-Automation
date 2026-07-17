import imaplib
import email
import re
import time
import os
from email.utils import parsedate_to_datetime
from datetime import datetime, timezone


def get_otp_from_email(sender_filter="theauthorizedpartner.com", timeout=60, poll_interval=3, since_start=None):
    host = os.getenv("EMAIL_IMAP_HOST")
    user = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_APP_PASSWORD")

    if not all([host, user, password]):
        raise EnvironmentError(
            "Missing EMAIL_IMAP_HOST, EMAIL_ADDRESS, or EMAIL_APP_PASSWORD in .env"
        )

    # Only accept emails that arrived AFTER the test started, so we never
    # accidentally grab a stale/old email.
    start_time = since_start or datetime.now(timezone.utc)

    end_time = time.time() + timeout
    while time.time() < end_time:
        mail = imaplib.IMAP4_SSL(host)
        mail.login(user, password)
        mail.select("inbox")

        # Search ALL (not just UNSEEN) so already-read emails aren't skipped
        status, data = mail.search(None, f'(FROM "{sender_filter}")')
        ids = data[0].split()

        # Walk newest-first so we check the most recent matching email first
        for msg_id in reversed(ids):
            status, msg_data = mail.fetch(msg_id, "(RFC822)")
            msg = email.message_from_bytes(msg_data[0][1])

            msg_date = parsedate_to_datetime(msg["Date"])
            if msg_date.tzinfo is None:
                msg_date = msg_date.replace(tzinfo=timezone.utc)

            if msg_date < start_time:
                # This email (and everything older, since we're newest-first
                # isn't guaranteed by IMAP id order, so just skip) is too old
                continue

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    if content_type == "text/plain":
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
                    elif content_type == "text/html" and not body:
                        raw_html = part.get_payload(decode=True).decode(errors="ignore")
                        body = re.sub(r"<[^>]+>", " ", raw_html)
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            otp_match = re.search(r"\b\d{6}\b", body)
            if otp_match:
                mail.logout()
                return otp_match.group()

        mail.logout()
        time.sleep(poll_interval)

    raise TimeoutError(
        f"No fresh OTP email from '{sender_filter}' received within {timeout}s"
    )