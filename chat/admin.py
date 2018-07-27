from django.contrib import admin
from .models import Room
from .models import OnlineUsers


admin.site.register(
    Room,
    list_display=["id", "title", "staff_only"],
    list_display_links=["id", "title"],
)



admin.site.register(
    OnlineUsers,
    list_display=["id", "title", "user"],
    list_display_links=["id", "title","user"],
)


