from django.contrib import admin
from .models import Post, Example, Category, Links

# Register your models here.
'''
https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
нужно создать суперпользователя? 
который имеет полный доступ к управлению сайтом?
python manage.py createsuperuser

Username: admin
Email address: admin@admin.com
Password: admin
Password (again): admin
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.






'''
admin.site.register(Post)




class ExampleAdmin(admin.ModelAdmin):
    # все поля которые должны отображаться в админ панели (дополнительные поля)
    list_display = ('id', 'title',  'photo', 'is_published', 'author', 'created_date' )
    list_display_links = ('id', 'title' , )
    search_fields = ('title', 'text')
    list_editable = ('author', 'is_published')

# Отвечает за вид админ панели
class CategoryAdmin(admin.ModelAdmin):
    # все поля которые должны отображаться в админ панели
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name', )
    search_fields = ('name',)

class LinksAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    list_display_links = ('id', 'link', )


"""
регистрируем блоки для админ панели, чтобы было видно на админ панели, 
для дальнейшей редактирование
первым предаем сам Модель, вторым передаем вспомогательный класс
"""
admin.site.register(Example, ExampleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Links, LinksAdmin)


