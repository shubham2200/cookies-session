from email.policy import default
import re
from django.shortcuts import render
from .models import *
from django.contrib.sessions import*

# Create your views here.


# def set_session(request):
#     request.session['name'] = 'shubham'
#     request.session['lname'] = 'bhalerao'

#     return render(request , 'set_session.html')


# def get_session(request):
#     name =  request.session.get( 'name')
#     lname =  request.session.get( 'lname')

#     return render( request , 'get_session.html' , {'name':name  , 'lname':lname})

# def del_session(request):
#     if 'name' in request.session:
#         del request.session['name']
#     return render( request , 'del_session.html' )



#  session key value method get and set,delete

# def set_session(request):
#     request.session['name'] = 'shubham'
#     request.session['last_name'] = 'bhalerao'

#     return render(request , 'set_session.html')


# def get_session(request):
#     name =  request.session.get( 'name')
#     lname =  request.session.get( 'last_name')
#     keys = request.session.keys()
#     items = request.session.items()

#     return render( request , 'get_session.html' , {'name':name ,'lname':lname, 'keys':keys , 'items':items} )

# def del_session(request):
#     request.session.flush()
#     return render( request , 'del_session.html' )



# django session cookies age expair method set get ,delete

def set_session(request):
    request.session['name'] = 'shubham'
    request.session.set_expiry(600)

    

    return render(request , 'set_session.html')


def get_session(request):
    name =  request.session.get( 'name')
    # print(request.session.get.session_cookie_age())
    # print(request.session.get.expiry_age())
    # print(request.session.get.expiry_date())
    # print(request.session.get.expiry_at_browser_close())
    return render( request , 'get_session.html' , {'name':name } )

def del_session(request):
    request.session.flush()
    request.session.clear_expired()
    return render( request , 'del_session.html' )
