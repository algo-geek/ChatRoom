from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate


# Create your views here.


def index(request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = User.objects.create_user(username=username,password=password)
            if user:
                return redirect('login')
    return render(request,'signup.html') 


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('index')
    return render(request,'login.html')

      
    

       