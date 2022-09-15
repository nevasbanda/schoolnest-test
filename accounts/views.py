from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_password = request.POST['conf_password']

        if password == conf_password:
            if User.objects.filter(username=username).exists():
                print('Username exists! try another username')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email is already taken! try another email')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=conf_password)
                    user.save()
                    return redirect('login')
        else:
            print('Password/Username did not matched')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('Login Successfully...!')
            return redirect('db_school')
        else:
            print('invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print('logged out from website')
        return redirect('login')


