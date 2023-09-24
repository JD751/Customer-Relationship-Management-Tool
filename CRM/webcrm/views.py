from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.models import auth


# Create your views here.


def home(request):
    return render(request, 'home.html')


	# Check to see if logging in
	# if request.method == 'POST':
	# 	username = request.POST['username']
	# 	password = request.POST['password']
	# 	# Authenticate
	# 	user = authenticate(request, username=username, password=password)
	# 	if user is not None:
	# 		login(request, user)
	# 		messages.success(request, "You Have Been Logged In!")
	# 		return redirect('home')
	# 	else:
	# 		messages.success(request, "There Was An Error Logging In, Please Try Again...")
	# 		return redirect('home')
	# else:
	# 	return render(request, 'webcrm/home.html',{} )

def register(request):
    form= UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('dashboard')
    
    context={'form':form}
    return render(request, 'register.html', context=context)


def user_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")


    context = {'form': form}

    return render(request, 'my-login.html', context=context)
    

def dashboard(request):
    pass

def user_logout(request):
    pass

