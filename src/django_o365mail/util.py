
import re
from django.core.mail.message import EmailMultiAlternatives
from . import settings

from email.mime.base import MIMEBase
from .file_mimebase import MIMEObjectToFileObject
from .file_tuple import TupleToFileObject

def string_contains_html(string):
    return (re.search(r'<.+?>', string) is not None)

def get_html_message(message):
    """
    Returns None if the email is plain text only, otherwise returns the HTML message
    """
    if type(message) == EmailMultiAlternatives:
        if message.alternatives:
            for alt in message.alternatives:
                if alt[1] == 'text/html':
                    return alt[0]
    return None

def get_message_body(message):
    """
    Function to get the body for the email message, depending on settings
    """
    html_body = get_html_message(message)
    if not html_body:
        if settings.O365_MAIL_REPLACE_LINE_ENDINGS and not string_contains_html(message.body):
            html_body = message.body.replace("\n", "<br />\n")
        else:
            html_body = message.body
    return html_body

def get_name_and_email(address):
    """
    Function to get name and email from addresses like
    Company <contact@company.com>, returned as tuple (name, email)
    """
    custom_sender_name = re.search(r'^([^<>]+)\s<([^<>]+)>$', address)
    if custom_sender_name:
        return custom_sender_name.group(1), custom_sender_name.group(2)
    else:
        return "", address

def get_converter(attachment):
    converter = None

    # Determine converter
    if isinstance(attachment, tuple):
        converter = TupleToFileObject
    elif isinstance(attachment, MIMEBase):
        converter = MIMEObjectToFileObject
    else:
        raise Exception("Invalid attachment type!")

    return converter