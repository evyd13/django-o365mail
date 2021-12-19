from django.core.mail import send_mail
from django.core.mail import EmailMessage, EmailMultiAlternatives
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from django.conf import settings


# Create your tests here.
to_email = "sixmoonskies@gmail.com"

def test_1():
    print("Sending a plain text message!")
    return send_mail(
        'Test 1',
        'Here is the message.',
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
        fail_silently=False,
    )

def test_2():
    print("Sending a plain text MULTILINE message!")
    return send_mail(
        'Test 2',
        "This\nemail message\nhas multiple\nlines.",
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
        fail_silently=False,
    )

def test_3():
    print("Sending a HTML message!")
    return send_mail(
        'Test 3',
        'Here is the message.',
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
        fail_silently=False,
        html_message="<p>Here's the html message</p>",
    )

def test_4():
    print("Sending a plain text message with attachment (text file)!")
    mail = EmailMessage(
        'Test 4',
        'This is the message',
        None,
        [to_email],
    )
    mail.attach("document.txt", b'This is the contents', 'text/plain')
    return mail.send(fail_silently=False)

def test_5():
    print("Sending a plain text message with multiple attachments!")
    mail = EmailMessage(
        'Test 5',
        'This is the message',
        None,
        [to_email],
    )
    mail.attach("document.txt", b'This is the contents', 'text/plain')
    mail.attach(MIMEText("This is the content of the second one!"))
    image = MIMEImage(open("{}{}".format(settings.STATIC_DIR, '/duck.jpg'), 'rb').read())
    image.add_header('Content-Disposition', "attachment; filename=duck.jpg")
    mail.attach(image)
    mail.attach_file("{}{}".format(settings.STATIC_DIR, '/bird.pdf'))
    mail.attach_file("{}{}".format(settings.STATIC_DIR, '/utf8.txt'))
    return mail.send(fail_silently=False)

def test_6():
    print("Sending an HTML message with inline and normal attachments!")
    mail = EmailMultiAlternatives(
        'Test 6',
        "This is the plain text message, you're missing out on a duck!",
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
    )
    # HTML message
    mail.attach_alternative("<p>Here's the html message</p><p>And here's an image of a duck:</p><br /><img src=\"cid:duck.jpg\">", 'text/html')

    # Attachments
    duck = MIMEImage(open("{}{}".format(settings.STATIC_DIR, '/duck.jpg'), 'rb').read())
    duck.add_header('Content-ID', 'duck.jpg')
    mail.attach(duck)
    mail.attach_file("{}{}".format(settings.STATIC_DIR, '/bird.pdf'))
    mail.attach_file("{}{}".format(settings.STATIC_DIR, '/utf8.txt'))
    return mail.send(fail_silently=False)

def test_7():
    print("Sending an HTML message (but differently)!")
    mail = EmailMessage(
        'Test 7',
        "<b>This is</b> <a href=\"https://google.com\">a link to Google</a> <i>which is cool</i>",
        None, # use settings.DEFAULT_FROM_EMAIL instead
        [to_email],
    )
    mail.content_subtype = 'html'
    return mail.send(fail_silently=False)