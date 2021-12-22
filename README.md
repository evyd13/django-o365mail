# django-o365mail

## Installation
Run the following on your system:

    pip install django-o365mail

Then, add these settings to your Django settings.py:

    EMAIL_BACKEND = 'django_o365mail.backend.O365EmailBackend'

    O365_MAIL_CLIENT_ID = 'REPLACE THIS'
    O365_MAIL_CLIENT_SECRET = 'REPLACE THIS'
    O365_MAIL_TENANT_ID = 'REPLACE THIS'

Mail can then be sent using the Django mail functions, as described [here](https://docs.djangoproject.com/en/3.2/topics/email/).

## Optional settings

### Mailbox
This module uses the `python-o365` library, which is also slightly customizable. Because of this you can define kwargs to be used when opening the mailbox. As an example:

    O365_MAIL_MAILBOX_KWARGS = {'resource': 'o365mailbox@domain.com'}

... which will be passed to the mailbox() function like this:

    account = O365.Account(credentials, auth_flow_type='credentials', tenant_id=self.tenant_id)
    mailbox = account.mailbox(**O365_MAIL_MAILBOX_KWARGS)

### Other
- `O365_MAIL_REPLACE_LINE_ENDINGS` (default: `True`)  
  Replaces line endings with an HTML line break (`<br />`) when emails are sent in plain text.
- `O365_MAIL_SAVE_TO_SENT` (default: `False`)  
  Saves sent emails to the 'Sent' folder.

## Sandbox
Create a file called `settings_secret.py` under the `sandbox/sandbox` directory (same directory as `settings.py`) with the settings as described above, except for the `EMAIL_BACKEND`. It could look like this:

    O365_MAIL_CLIENT_ID = 'REPLACE THIS'
    O365_MAIL_CLIENT_SECRET = 'REPLACE THIS'
    O365_MAIL_TENANT_ID = 'REPLACE THIS'

Then, if needed, add settings to `settings.py`.

To be able to make changes to this module, run the following command to install this module in editable mode:

    pip install -e ./

And run the sandbox server:

    cd sandbox && python manage.py runserver

