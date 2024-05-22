from django.urls import path
from . import views
from .views import sendCommands

urlpatterns = [
    path("", sendCommands().home, name="home"),
    path('data/', sendCommands().send, name="data"),
]
