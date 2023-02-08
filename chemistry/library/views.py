from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles
from django.views.generic import DetailView, UpdateView


def tasks(request):
    task = Articles.objects.all()[1:]
    return render(request, 'library/tasks.html', {'task': task})

def library_home(request):
    text = Articles.objects.all()[:0]
    return render(request, 'library/library_home.html', {'text': text})

def tests(request):
    if request.method == 'POST':
        test = ArticlesForm(request.POST)
        if test.is_valid():
            print('hello world')
    else:
        print('error')



class LibraryDetailView(DetailView):
    model = Articles
    template_name = 'library/details_view.html'
    context_object_name = 'article'

class LibraryUpdateView(UpdateView):
    model = Articles
    template_name = 'library/add.html'
    form_class = ArticlesForm

def add(request):
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ArticlesForm()
    context = {
        'form': form
    }
    return render(request, 'library/add.html', context)

