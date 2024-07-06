from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from UserAuthentication.forms import UserForm, LoginForm
# Create your views here.

def login(request):
    if request.method == 'GET':
        items = {
        'form': LoginForm()
        }   
        return render(request, 'UserAuthentication/signin.html', context=items)
    elif request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('index')
        else:
            return render(request, 'UserAuthentication/signin.html', {'form': form})
    else:
        print(form.errors)
        return render(request, 'UserAuthentication/signin.html', {'form': form})
def register(request):
    if request.method == 'GET':
        items = {
        'form': UserForm()
        }   
        return render(request, 'UserAuthentication/signup.html', context=items)
    elif request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'UserAuthentication/signin.html')
        
        
def logout(request):
    logout_user(request)
    return redirect('login')
   
