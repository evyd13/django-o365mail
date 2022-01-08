from django.http import HttpResponse
from django.conf import settings
from .tests import *
from .tests import TEST_FUNCTION_PREFIX
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
            if key.startswith(TEST_FUNCTION_PREFIX):
                tests_to_run.append(key)

    if isinstance(tests_to_run, list):
        for i in range(len(tests_to_run)):
            if str(tests_to_run[i]).startswith(TEST_FUNCTION_PREFIX):
                tests_to_run[i] = str(tests_to_run[i])[len(TEST_FUNCTION_PREFIX):]

    for test in tests_to_run:
        tests_run_count += 1
        function = globals().get("".join([TEST_FUNCTION_PREFIX, test]))
        sent = function()
        if sent:
           tests_succes_count += 1
        print("")

    return (tests_run_count - tests_succes_count), tests_run_count