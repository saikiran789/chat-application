from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Room
import json
from .models import OnlineUsers
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers

User = get_user_model()

@login_required
def index(request):

    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")
    #usersOnline = User.objects.all()
    #console.log(usersOnline)
    # Render that in the index template

    return render(request, "index.html", {
        "rooms": rooms	
     })

def userlist(request):
    #onlineuser=[]
    #onlineuser = OnlineUsers.objects.filter(user="sahithi")
    room_id=2
    records = OnlineUsers.objects.filter(title=room_id)
    json_res = []
    for record in records:
        json_obj = record.user
        json_res.append(json_obj)
        json_stuff=json.dumps(json_res,indent=2)
        print(json_stuff)
    return HttpResponse(json_stuff,content_type='application/json')

def userlist_o(request):
    #onlineuser=[]
    #onlineuser = OnlineUsers.objects.filter(user="sahithi")
        room_id=2
        data = serializers.serialize('json', OnlineUsers.objects.filter(title=room_id))
        #onlineUsers = OnlineUsers.objects.filter(title=room_id).values('user')
        #serializers.serialize('json', events)
        print("Hello World",data)
        return HttpResponse(json.dumps(data))
    

def user_list_01(request):
    """
    NOTE: This is fine for demonstration purposes, but this should be
    refactored before we deploy this app to production.
    Imagine how 100,000 users logging in and out of our app would affect
    the performance of this code!
    """
    users = User.objects.select_related('logged_in_user')
    for user in users:
        user.status = 'Online' if hasattr(user, 'logged_in_user') else 'Offline'
    return render(request, 'templates/registration/user_list.html', {'users': users})

def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('user_list'))
        else:
            print(form.errors)
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def log_out(request):
    logout(request)
    return redirect(reverse('templates/registration:login'))


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('templates/registration:log_in'))
        else:
            print(form.errors)
    return render(request, 'templates/registration/sign_up.html', {'form': form})
