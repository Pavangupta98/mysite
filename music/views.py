from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from music.forms import Registration_form
from django.contrib.auth.models import User
from twilio.rest import Client


def home(request):
    return render(request, 'music/home.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'music/profile.html', {"args":user})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    form = Registration_form(request.POST)
    args = {'form': form}
    return render(request, 'music/login.html',{"form":form})




def register(request):
    if request.method == 'POST':
        form = Registration_form(request.POST)
        if form.is_valid():
            saveit = form.save(commit=False)
            saveit.save()
            subject = 'verification'
            message = 'Welcome to my world Pavan !'
            from_email = settings.EMAIL_HOST_USER
            to_list = [saveit.email, 'pavangupta1997ng@gmail.com']
           
            send_mail(subject=subject, message=message, from_email=from_email,recipient_list=to_list, fail_silently=False)
            account_sid = "AC46989a2efd005d718d4b8e0bfb12ce62"
            auth_token = "3be9277bedae40879626bc0f60371303"

            client = Client(account_sid, auth_token)

            client.messages.create(
                to="+917999736575",
                from_="+918989445058",
                body="This is the ship that made the Kessel Run in fourteen parsecs?"
            )

            return render(request, 'music/home.html')
    else:
        form = Registration_form

        args = {'form': form}
        return render(request, 'music/registration_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'music/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/music/profile/')
    else:
        form = UserChangeForm(instance=request.user)

        args = {'form': form}
        return render(request, 'music/edit_profile.html', args)