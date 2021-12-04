from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testMail(request):
    from django.core.mail import send_mail

    mail_sent = send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return HttpResponse(mail_sent)