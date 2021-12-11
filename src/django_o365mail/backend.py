import threading

from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
import O365

"""
A wrapper that manages the O365 API for sending emails.
Uses an identity (auth_flow_type == 'credentials').
See https://docs.microsoft.com/en-us/graph/auth-v2-service?context=graph%2Fapi%2F1.0&view=graph-rest-1.0 for more details.
"""

class O365EmailBackend(BaseEmailBackend):
    def __init__(self, client_id=None, client_secret=None, tenant_id=None,
                 fail_silently=False, **kwargs):
        super().__init__(fail_silently=fail_silently)
        self.client_id = client_id or settings.O365_MAIL_CLIENT_ID
        self.client_secret = client_secret or settings.O365_MAIL_CLIENT_SECRET
        self.tenant_id = tenant_id or settings.O365_MAIL_TENANT_ID

        self.mailbox = None
        self._lock = threading.RLock()

    def open(self):
        """
        Ensure an open connection to the email server. Return whether or not a
        new connection was required (True or False) or None if an exception
        passed silently.
        """
        if self.mailbox:
            # Nothing to do if the mailbox is already open.
            return False

        credentials = (self.client_id, self.client_secret)
        account = O365.Account(credentials, auth_flow_type='credentials', tenant_id=self.tenant_id)
        try:
            if account.authenticate():
                self.mailbox = account.mailbox()
                return True
        except:
            if not self.fail_silently:
                raise

    def close(self):
        pass

    def send_messages(self, email_messages):
        if not email_messages:
            return 0
        with self._lock:
            new_mailbox_created = self.open()
            if not self.mailbox or new_mailbox_created is None:
                return 0
            num_sent = 0
            for message in email_messages:
                sent = self._send(message)
                if sent:
                    num_sent += 1
            if new_mailbox_created:
                self.close()
        return num_sent

    def _send(self, email_message):
        """A helper method that does the actual sending."""
        print(message.__dict__)
        # if not email_message.recipients():
        #     return False
        # encoding = email_message.encoding or settings.DEFAULT_CHARSET
        # from_email = sanitize_address(email_message.from_email, encoding)
        # recipients = [sanitize_address(addr, encoding) for addr in email_message.recipients()]
        # message = email_message.message()
        # try:
        #     self.connection.sendmail(from_email, recipients, message.as_bytes(linesep='\r\n'))
        # except smtplib.SMTPException:
        #     if not self.fail_silently:
        #         raise
        #     return False
        # return True
        return True
