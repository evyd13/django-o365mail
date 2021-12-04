from django.core.mail.backends.base import BaseEmailBackend
import O365


"""
A wrapper that manages the O365 API for sending emails.
Uses an identity (auth_flow_type == 'credentials').
See https://docs.microsoft.com/en-us/graph/auth-v2-service?context=graph%2Fapi%2F1.0&view=graph-rest-1.0 for more details.
"""

class O365EmailBackend(BaseEmailBackend):
    def open(self):
        pass
    def close(self):
        pass
    def send_messages(self, email_messages):
        pass