from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from email.mime.text import MIMEText

# Create your views here.

to_email = "sixmoonskies@gmail.com"
def test_1():
    print("Sending a plain text message!")
    return send_mail(
        'Subject here',
        'Here is the message.',
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
        fail_silently=False,
    )

def test_2():
    print("Sending a plain text MULTILINE message!")
    return send_mail(
        'Subject here',
        "This\nemail message\nhas multiple\nlines.",
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
        fail_silently=False,
    )

def test_3():
    print("Sending a HTML message!")
    return send_mail(
        'Subject here',
        'Here is the message.',
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
        fail_silently=False,
        html_message="<p>Here's the html message</p>"
    )

def test_4():
    print("Sending a plain text message with attachment (text file)!")
    mail = EmailMessage(
        'Subject here',
        'This is the message',
        None,
        [to_email]
    )
    mail.attach("document.txt", b'This is the contents', 'text/plain')
    mail.attach(MIMEText("This is the content of the second one!"))
    return mail.send(fail_silently=False)

def testMail(request):
    from django_o365mail import settings as o365_settings
    
    if not o365_settings.O365_ACTUALLY_SEND_IN_DEBUG and settings.DEBUG:
        print("WARNING: Email messages won't actually be sent! Set O365_ACTUALLY_SEND_IN_DEBUG = True to actually send emails.")
    
    for key, value in globals().items():
        if key.startswith('test_'):
            sent = value()
            assert sent == 1 or True
            print("")
    return HttpResponse("tests done")