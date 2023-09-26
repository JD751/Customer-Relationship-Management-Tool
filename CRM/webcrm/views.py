from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,login
from django.contrib import messages
from .forms import UserCreationForm, LoginForm



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
            return redirect('login')
    
    context={'form':form}
    return render(request, 'register.html', context=context)


def user_login(request):

    form = LoginForm()
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(form.cleaned_data)

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")
            else:
                error_message = "Invalid username or password."

    context = {'form': form, 'error_message': error_message}
    print(error_message)
    
    return render(request, 'user_login.html', context=context)

    

def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('home')

