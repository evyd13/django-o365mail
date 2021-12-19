from django.http import HttpResponse
from django.conf import settings
from .tests import *
# Create your views here.

def testMail(request):
    from django_o365mail import settings as o365_settings
    
    if not o365_settings.O365_ACTUALLY_SEND_IN_DEBUG and settings.DEBUG:
        print("WARNING: Email messages won't actually be sent! Set O365_ACTUALLY_SEND_IN_DEBUG = True to actually send emails.")
    
    failed, ran = run_tests(['all'])
        
    return HttpResponse("{} out of {} tests ran without errors.".format(ran - failed, ran))

def run_tests(tests_to_run):
    tests_run_count = 0
    tests_succes_count = 0
    if tests_to_run == 'all' or 'all' in tests_to_run:
        tests_to_run = []
        for key in list(globals().keys()):
            if key.startswith('test_'):
                tests_to_run.append(key)

    for test in tests_to_run:
        tests_run_count += 1
        function = globals().get(test, globals().get('test_' + str(test)))
        sent = function()
        if sent:
            tests_succes_count += 1
        print("")

    return (tests_run_count - tests_succes_count), tests_run_count