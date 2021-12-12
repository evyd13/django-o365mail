from django.core.mail.backends.base import BaseEmailBackend
import threading
import O365

from . import settings
from . import util

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
                kwargs = settings.O365_MAIL_MAILBOX_KWARGS
                self.mailbox = account.mailbox(**kwargs)
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
        if not email_message.recipients():
            return False

        # Basic email information
        m = self.mailbox.new_message()
        m.to.add(email_message.to)
        m.cc.add(email_message.cc)
        m.bcc.add(email_message.bcc)

        m.sender.name, m.sender.address = util.get_name_and_email(email_message.from_email)
        m.subject = email_message.subject
        m.body = util.get_message_body(email_message)
        
        # Attachments
        if email_message.attachments:
            for attachment in email_message.attachments:
                converter = util.get_converter(attachment)(attachment)
                file = converter.get_file()
                filename = converter.get_filename()
                m.attachments.add([(file, filename)])
        
        # Send it!
        try:
            if (settings.DEBUG and settings.O365_ACTUALLY_SEND_IN_DEBUG) or not settings.DEBUG:
                return m.send(save_to_sent_folder=settings.O365_MAIL_SAVE_TO_SENT)
            return True
        except Exception as e:
            if self.fail_silently:
                return False
            raise e
