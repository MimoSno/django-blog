from django import forms

from .models import Example,Links

'''
импортируем формы Django (from django import forms)

ExampleForm - это имя для нашей формы

forms.ModelForm - сообщить Django, что эта форма относится к ModelForm (таким способом, мы добавляем свою форму)

ModelForm - можем создать новую форму с нуля или воспользоваться для сохранения содержимого формы в модель

Model Meta — это, по сути, внутренний класс вашего модельного класса. 
Мета модели в основном используется для изменения поведения полей вашей модели, 
таких как изменение параметров порядка, verbose_name и многих других параметров.


class Meta, где определяем, какая модель будет использоваться для создания формы (model = Example).

'''


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = ('title', 'text', 'author', 'category_data', 'photo',)

class LinkForm(forms.ModelForm):
    class Meta:
        model = Links
        fields = ('name', 'link')
