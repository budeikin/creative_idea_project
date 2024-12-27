from django.shortcuts import render
from django.views.generic import ListView
from .models import Silo


# Create your views here.

class SiloListView(ListView):
    template_name = 'silo/silo_list.html'
    model = Silo



