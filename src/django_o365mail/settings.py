from django.conf import settings

defaults = {
    'DEBUG': False,
    'O365_MAIL_CLIENT_ID': None,
    'O365_MAIL_CLIENT_SECRET': None,
    'O365_MAIL_TENANT_ID': None,
    'O365_MAIL_MAILBOX_KWARGS': {},
    'O365_MAIL_REPLACE_LINE_ENDINGS': True,
    'O365_MAIL_SAVE_TO_SENT': False,
    'O365_ACTUALLY_SEND_IN_DEBUG': False,
    'O365_SUBJECT_PREFIX': '',
}

for key, value in list(defaults.items()):
    if not hasattr(settings, key):
        globals()[key] = value
    else:
        globals()[key] = getattr(settings, key)
