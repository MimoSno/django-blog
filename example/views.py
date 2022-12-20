from django.utils import timezone
from .models import Example
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ExampleForm
# Create your views here.

'''
https://docs.djangoproject.com/en/1.11/topics/http/views/

Подробнее о QuerySets в Django можно узнать в официальной документации: 
https://docs.djangoproject.com/en/1.11/ref/models/querysets/

get_object_or_404:
В случае, если не существует экземпляра объекта Example с заданным pk, 
мы получим намного более приятную страницу (которая называется Page Not Found 404) 
Вместо такой ошибки можно с помощью get_object_or_404 можно вывести на страницу Page not found


'''


def index_list(request):
    # получаем из БД отфильтрованные данные
    examples = Example.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # параметр request - всё, что мы получим от пользователя в качестве запроса через Интернет
    return render(request, 'example/index_list.html', {'examples': examples})

def example_detail(request, pk):
    print(pk)
    example = get_object_or_404(Example, pk=pk)
    return render(request, 'example/example_detail.html', {'example': example})

def documentation(request):
    return render(request, 'example/documentation.html')


def example_new(request):
    if request.method == "POST":
        form = ExampleForm(request.POST, request.FILES or None)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            example = form.save(commit=False)
            print(example)
            example.author = request.user
            print(example)
            example.published_date = timezone.now()
            print(example)
            example.save()
            print(example)
            return redirect('example_detail', pk=example.pk)
    else:
        form = ExampleForm()
    return render(request, 'example/example_edit.html', {'form': form})


def businessmans(request):
    businessman = Example.objects.all()
    return render(request, 'example/tags/businessman.html', {'bus': businessman})

def it(request):
    return render(request, 'example/tags/it.html', {})