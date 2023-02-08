from django.shortcuts import render, redirect
from .forms import MassiveForm
from .models import Massive
from django.views.generic import DetailView



def index(request):
    return render(request, 'main/index.html')

def theory(request):
    words = Massive.objects.all()
    return render(request, 'main/theory.html', {'words': words})

class TheoryDetailView(DetailView):
    model = Massive
    template_name = 'main/theory_detail.html'
    context_object_name = 'massive'

def links(request):
    return render(request, 'main/links.html')


def task(request):
    return render(request, 'main/tasks.html')


