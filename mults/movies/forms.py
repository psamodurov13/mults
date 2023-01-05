from django import forms
from .models import Category, Tags, Movies
import requests as rq
import re
from django.core.exceptions import ValidationError


class ContactForm(forms.Form):
    email = forms.EmailField(label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MoviesForm(forms.ModelForm):
    class Meta:
        model = Movies
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'default_rate', 'age', 'country', 'year', 'trailer', 'serial',
                  'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'default_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'trailer': forms.URLInput(attrs={'class': 'form-control'}),
            'serial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title

    # title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(label='Описание', required=False, widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'rows': 5
    # }))
    # # photo = forms.ImageField(upload_to='photos/movies_thumb/%Y/%m/%d/', verbose_name="Фото", blank=True)
    # is_published = forms.BooleanField(label='Опубликовано', initial=True, widget=forms.CheckboxInput(attrs={
    #     'class': 'form-check-input'
    # }))
    # default_rate = forms.FloatField(label='Рейтинг', required=False, widget=forms.NumberInput(attrs={
    #     'class': 'form-control'
    # }))
    # age = forms.IntegerField(label='Возраст', required=False, widget=forms.NumberInput(attrs={
    #     'class': 'form-control'
    # }))
    # country = forms.CharField(label='Страна', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # year = forms.IntegerField(label='Год', required=False, widget=forms.NumberInput(attrs={
    #     'class': 'form-control'
    # }))
    # trailer = forms.CharField(label='Трейлер', required=False, widget=forms.URLInput(attrs={'class': 'form-control'}))
    # serial = forms.BooleanField(label='Сериал', required=False, widget=forms.CheckboxInput(attrs={
    #     'class': 'form-check-input'
    # }))
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
    #                                   empty_label='Выберите категорию', widget=forms.Select(attrs={
    #         'class': 'form-control'
    #     }))
    # tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), label='Теги', required=False,
    #                                       widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

