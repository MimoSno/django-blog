from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

'''
models.Model - объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных

свойства - title, text, created_date, published_date и author

Последним шагом будет добавление нашей модели в базу данных. 
Сначала мы должны дать Django знать, что сделали изменения в нашей модели (мы её только что создали!). 
Набери: python manage.py makemigrations

Django создал для нас файл с миграцией для базы данных. 
Набери python manage.py migrate


Если добавили в БД новую таблицу или столбцы, 
провести: python manage.py makemigrations и python manage.py migrate


Добавляем в БД новые строки: 

Открой свой локальный терминал и набери следующую команду:

python manage.py shell

Ты находишься в интерактивной консоли Django. 
По сути, это та же интерактивная консоль Python, но с магией Django :) 
Ты можешь использовать весь синтаксис Python, разумеется.

from example.models import Example - не забудь импортировать класс(таблицу) в консоль
from django.contrib.auth.models import User - будет отвечать за автора записи

User.objects.all() - показывает какие пользователи  есть в нашей базе данных
У тебя должен появиться: <QuerySet [<User: admin>]> - Это суперпользователь, которого мы создали ранее! Нам нужен его экземпляр:
me = User.objects.get(username='admin')


Example.objects.all() - вывести на экран все записи
Example.objects.create(author=me, title='Sample title', text='Test') - Создать объект Post в базе данных (добавить строку в таблицу)



QuerySets является возможность фильтровать объекты
нам нужно найти все записи пользователя admin. 
Мы используем метод filter вместо метода all в Post.objects.all(). 
В скобках мы укажем условия, по которым будет построена выборка записей. 
В нашей ситуации условием будет являться равенство поля author переменной me. 
В Django мы можем написать это следующим образом: author=me. 
Теперь наш код выглядит следующим образом:

Example.objects.filter(author=me) - получаем все данные связанные с автором админ
вывод: <QuerySet [<Example: Elon Reeve Musk>, <Example: Jeffrey Preston Bezos>, <Example: Jeffrey Preston Bezos>, <Example: Jeffrey Preston Bezos>, <Example: Bill Gates>]>

Example.objects.filter(title__contains='title') - все записи со словом 'title' в поле title
вывод: <QuerySet []> - у меня пустой, я ничего не добавила в столбец title co словом "title"

Примечание: 
обрати внимание на два символа нижнего подчёркивания (_) между title и contains. 
Django ORM использует этот синтаксис для разделения имён полей ("title") и операций или фильтров ("contains"). 
Если ты используешь только один символ нижнего подчёркивания, 
то получишь ошибку "FieldError: Cannot resolve keyword title_contains".



from django.utils import timezone - подключаем из джанго время (получаем список всех опубликованных записей)

Example.objects.filter(published_date__lte=timezone.now()) - отфильтруем записи по полю published_date
вывод: <QuerySet []> - еще мы ничего не опубликовали, чтобы опубликовать должны выбрать, что хотим опубликовать
Например:
example = Example.objects.get(title="Elon Reeve Musk")

Дальше мы опубликуем её с помощью метода publish - этот метод наша функция внутри нашего класса внизу 
example.publish()

теперь отправляем запрос: 
Example.objects.filter(published_date__lte=timezone.now())
вывод: <QuerySet [<Example: Elon Reeve Musk>]>

Example.objects.order_by('created_date') - QuerySets позволяет сортировать объекты
Example.objects.order_by('-created_date') -  можем изменить порядок на противоположный, добавив - в начало условия

Соединение QuerySets
QuerySets можно сцеплять, создавая цепочки
Example.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
вывод: <QuerySet [<Example: Elon Reeve Musk>]> - такой пример подойдет, если мы опубликуем несколько записей 

Чтобы закрыть интерактивную консоль, набери: exit()


Админ панели:

verbose_name - отвечает за названия столбцов в админ панели 
verbose_name - название таблицы в админ панели в единственном числе
verbose_name_plural - название таблицы в админ панели во множественном числе
ordering - сортировка данных в админ панели внутри таблицы, такая сортировка по умолчанию применяется для самого сайта тоже


'''


class Post(models.Model):
    # по этой ссылке все документации по типом полей https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types
    # models.ForeignKey — ссылка на другую модель
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # текстовое поле с ограничением на количество символов
    title = models.CharField(max_length=200)
    # поле для неограниченно длинного текста
    text = models.TextField()
    # дата и время
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


    # метод публикации для записи
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # получим текст (строку) с заголовком записи
    def __str__(self):
        return self.title


class Example(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='aвтор')
    title = models.CharField(max_length=200, unique=True ,verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='dата создание')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата публикации')
    category_data = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категории')
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d')
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # получим текст (строку) с заголовком записи
    def __str__(self):
        return self.title
    '''
    помогает в админ панели ставить кнопку 
    "смотреть на сайте", еще для многих других задач используется функция
    '''
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    # Настройка для модели (можно название столбцов изменить, название БД, также можно для админ панели использовать)
    class Meta:
        verbose_name = 'Бизнесмен' # единственная
        verbose_name_plural = 'Бизнесмены' # множественная
        """
        ordering - порядок сортировки, сначала сортировка будет по created_date, 
        если одинаковые  уровни то преходит к следующему
        """
        ordering = ['created_date', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория' # единственная
        verbose_name_plural = 'Категории' # множественная
        ordering = ['id']

class Links(models.Model):
    name = models.ForeignKey('Example', on_delete=models.PROTECT, to_field='title', verbose_name='Имя')
    def __str__(self):
        return self.name
    link = models.URLField(verbose_name='Ссылка')
    class Meta:
        verbose_name = 'Cсылка'
        verbose_name_plural = 'Ссылки'
        ordering = ['id']