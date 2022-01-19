import re
from django.shortcuts import render

# Create your views here.
def set_test_cookie(request):
    request.session.set_test_cookie()
    return render( request , 'set_test_cookie.html' )

def check_test_cookie(request):
    request.session.set_test_cookie()
    return render( request , 'check_test_cookie.html' )

def del_test_cookie(request):
    request.session.set_test_cookie()
    return render( request , 'del_cookie.html' )