from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Object

class IndexView(generic.ListView):
    template_name = 'repository/index.html'
    context_object_name = 'repository_list'


class DetailView(generic.DetailView):
    model = Object
    template_name = 'repository/detail.html'