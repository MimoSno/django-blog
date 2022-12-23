from django.utils import timezone
from .models import Example
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

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
    links = Links.objects.all()
    # параметр request - всё, что мы получим от пользователя в качестве запроса через Интернет
    return render(request, 'example/index_list.html', {'examples': examples, 'links': links})


def example_detail(request, pk):
    print(pk)
    example = get_object_or_404(Example, pk=pk)
    return render(request, 'example/example_detail.html', {'example': example})


def documentation(request):
    return render(request, 'example/documentation.html')


def example_new(request):
    if request.method == "POST":
        form_post = ExampleForm(request.POST, request.FILES or None)
        form_link = LinkForm(request.POST)

        if form_post.is_valid():
            example = form_post.save(commit=False)
            example.author = request.user
            example.published_date = timezone.now()
            example.save()
            return redirect('example_detail', pk=example.pk)
        if form_link.is_valid():
            link = form_link.save(commit=False)
            link.author = request.user
            link.published_date = timezone.now()
            link.save()
    else:
        form_post = ExampleForm()
        form_link = LinkForm()
    return render(request, 'example/example_edit.html', {'form_post': form_post, 'form_link': form_link})


def businessmans(request):
    businessman = Example.objects.all()
    return render(request, 'example/tags/businessman.html', {'bus': businessman})


def it(request):
    return render(request, 'example/tags/it.html', {})
