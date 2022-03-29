from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Balance
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

# login

def login(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password'] 

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')

    else:
       return render(request, 'pages/login.html')

# logout

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')



# sign up

def signup(request):
  if request.method == 'POST':
    # get form values
    first_name = request.POST['first_name'] 
    last_name = request.POST['last_name'] 
    username = request.POST['username'] 
    email = request.POST['email'] 
    password = request.POST['password'] 
    password2 = request.POST['password2'] 

    # check password match
    if password == password2:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already exist')
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email already exist')
            return redirect('signup')
            
        else:
            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            return redirect('login')

    else:
        messages.info(request, 'Password does not match')
        return redirect('signup')

  else:
    return render(request, 'pages/signup.html')


    
@login_required
def withdraw(request):
    return render(request, 'pages/withdraw.html')

@login_required
def deposit(request):
    return render(request, 'pages/deposit.html')

@login_required
def bnb(request):
    return render(request, 'pages/bnb.html')

@login_required
def btc(request):
    return render(request, 'pages/btc.html')

@login_required
def eth(request):
    return render(request, 'pages/eth.html')

@login_required
def sol(request):
    return render(request, 'pages/sol.html')

@login_required
def usdt(request):
    return render(request, 'pages/usdt.html')

@login_required
def dashboard(request):
    balance = Balance.objects.all()
    return render(request, 'pages/Dashboard.html', {'balance': balance})
