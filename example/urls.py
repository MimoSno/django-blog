from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
'''
post/ значит, что после начала строки URL должен содержать слово post и косую черту /. 
Пока всё в порядке.

<int:pk> — Django ожидает целочисленное значение и преобразует его в представление — переменную pk.




'''


urlpatterns = [
    path('', views.index_list, name='index_list'),
    path('example/<int:pk>/', views.example_detail, name='example_detail'),
    path('documentation/', views.documentation, name='documentation'),
    path('example/new/', views.example_new, name='example_new'),
    path('example/businessman/', views.businessmans, name='Businessman'),
    path('example/it/', views.it, name='IT'),
]


'''
urlpatterns = [
    path('', views.index_list, name='index_list'),
    path('example/<int:pk>/', views.example_detail, name='example_detail'),
    path('documentation/', views.documentation, name='documentation'),
    path('example/new/', views.example_new, name='example_new'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''