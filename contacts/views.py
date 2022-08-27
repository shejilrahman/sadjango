from django.shortcuts import render
from .models import Member

from django.views.generic import ListView


class HomePageView(ListView):
    model = Member
    template_name = 'home.html'

    

# Create your views here.
