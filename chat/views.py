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



