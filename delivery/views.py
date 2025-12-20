from django.http import HttpResponse
from django.shortcuts import render
from django.db import IntegrityError
from .models import User

# Create your views here.
def index(request):
    return render(request, "index.html")

def open_signup(request):
    return render(request, "signup.html")

def open_signin(request):
    return render(request, "signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        if User.objects.filter(email=email).exists():
            return HttpResponse("This Email is already registered. Please use a different email.")

        user = User(username=username, password=password, email=email,mobile=mobile, address=address)
        user.save()

        # return HttpResponse(f"Sign Up Successful!!, Data saved")
        return render(request, "signin.html")
    
    else:
        return HttpResponse("Invalid Response")
    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            request.session['username'] = user.username
            
            if user.username == 'admin':
                return render(request, 'admin_home.html')
            else:
                return render(request, 'customer_home.html')

        except User.DoesNotExist:
            return render(request, 'fail.html')

    return render(request, 'signin.html')

    
def open_add_restaurant(request):
    return render(request, 'add_restaurant.html')
        