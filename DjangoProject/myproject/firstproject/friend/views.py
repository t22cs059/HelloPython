from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore
from .models import Friend
from django.views.generic import ListView, DetailView

class FriendList(ListView):
    model = Friend
    
class FrinedDetail(DetailView):
    model = Friend
