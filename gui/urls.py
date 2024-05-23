from django.urls import path
from . import views
from .views import sendCommands

urlpatterns = [
    path("", sendCommands().home, name="base"),
    path("index.html", sendCommands().send, name="index"),
]
