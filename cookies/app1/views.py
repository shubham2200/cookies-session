import datetime
from django.shortcuts import render
from datetime import*
# Create your views here.

def set_cookie(request):
    response = render( request , 'setcookie.html')
    # response.set_cookie('name' , 'shubham', max_age=30) this max_age is a time for expair..
    response.set_cookie('name' , 'shubham', expires=datetime.utcnow()+ timedelta(days=2))
    return response


# here we have many type of to get the cookies  3rd one are take extra string if cookie are delete then that string show 
def get_cookie(request):
    # name = request.COOKIES['name']
    # name = request.COOKIES.get('name')
    name = request.COOKIES.get('name' , 'guest')
    return render( request , 'get_cookie.html', { 'name':name } )

# here we going delete the cookie how we want .. hum cookie aapna tarika se delete kar sarkta he handle kar sakta he
def del_cookie(request):
    response = render( request , 'del_cookie.html' )
    response.delete_cookie('name')
    return response