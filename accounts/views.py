from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required

# Create your views here.
dashboard_url = 'dash'


def about(req):
    return render(req, 'accounts/about.html')


def home(req):
    args = {
        'current': 'current'
    }
    return render(req, 'accounts/home.html', args)


def signup(req):
    return render(req, 'accounts/signup.html')


def contact(req):
    return render(req, 'accounts/contact.html')


def signin(request):
    if(request.user.is_authenticated):
        return redirect(dashboard_url)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(dashboard_url)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.refresh_from_db()  # load the profile instance created by the signal
            # user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            return redirect('register_success')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required(login_url='/signin/')
def userLogout(request):
    logout(request)
    return redirect('signin')



def register_success(request):
    if(request.user.is_authenticated):
        return redirect(dashboard_url)
    else:
        context = {
            'success': "Successfully"
        }
        return render(request, 'accounts/signup.html', context)
