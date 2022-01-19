import datetime
from django.shortcuts import render
from datetime import*
# Create your views here.

def set_cookie(request):
    response = render( request , 'set_signed_cookie.html')
    response.set_signed_cookie('name' , 'shubham',salt='nm', expires=datetime.utcnow()+ timedelta(days=2))
    return response


# here we have many type of to get the cookies  3rd one are take extra string if cookie are delete then that string show 
def get_cookie(request):
    name = request.get_signed_cookie('name' ,salt='nm' )
    
    
    return render( request , 'get_signed_cookie.html', { 'name':name } )

# here we going delete the cookie how we want .. hum cookie aapna tarika se delete kar sarkta he handle kar sakta he
# def del_cookie(request):
#     response = render( request , 'del_cookie.html' )
#     response.delete_cookie('name')
#     return response