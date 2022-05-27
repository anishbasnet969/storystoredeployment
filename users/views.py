from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser


# Create your views here.
def signupview(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if CustomUser.objects.filter(username=username):
            messages.error(request, "Username already exists! Try another username.")
            return redirect('signup')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Password didn't match!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, 'Username must contain both letters and numbers!!!')
            return redirect('signup')

        newuser = CustomUser.objects.create_user(username, email, pass1)
        newuser.save()
        messages.success(request, "Your Account has been created succesfully!!")

        return redirect('signin')
    
    return render(request, 'registration/signup.html')

def signinview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'Incorrect Credentials!!')
            return redirect('signin')
    
    return render(request, 'registration/signin.html')

def signoutview(request):
    logout(request)
    messages.success(request, "Logged out Successfully!!")
    return redirect('home')