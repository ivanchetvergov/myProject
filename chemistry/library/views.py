from django.shortcuts import render, redirect
from .forms import ArticlesForm
from .models import Articles
from django.views.generic import DetailView, UpdateView

def about(request):
    return render(request, 'library/about.html')

def tasks(request):
    task = Articles.objects.filter(key='properties')
    return render(request, 'library/tasks.html', {'task': task})

def tasks1(request):
    task1 = Articles.objects.filter(key='second')
    return render(request, 'library/tasks1.html', {'task1': task1})

def tasks2(request):
    task2 = Articles.objects.filter(key='third')
    return render(request, 'library/tasks2.html', {'task2': task2})

def tasks3(request):
    task3 = Articles.objects.filter(key='4')
    return render(request, 'library/tasks3.html', {'task3': task3})

def tasks4(request):
    task4 = Articles.objects.filter(key='5')
    return render(request, 'library/tasks4.html', {'task4': task4})

def tasks5(request):
    task5 = Articles.objects.filter(key='6')
    return render(request, 'library/tasks5.html', {'task5': task5})

def tasks6(request):
    task6 = Articles.objects.filter(key='7')
    return render(request, 'library/tasks6.html', {'task6': task6})

def tasks7(request):
    task7 = Articles.objects.filter(key='8')
    return render(request, 'library/tasks7.html', {'task7': task7})

def library_home(request):
    text = Articles.objects.all()[0:0]
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


