from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Movies, Category, Tags


class MoviesAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Movies
        fields = '__all__'


# Register your models here.
class MoviesAdmin(admin.ModelAdmin):
    form = MoviesAdminForm
    list_display = ('id', 'title', 'category', 'created_at', 'is_published', 'serial', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published', 'category')
    list_filter = ('is_published', 'category', 'tags')
    fields = ('title', 'category', 'content', 'photo', 'get_photo', 'is_published', 'serial', 'default_rate', 'age',
              'country', 'year', 'genre', 'director', 'time', 'actors', 'related', 'trailer', 'tags', 'views',
              'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'no photo'

    get_photo.short_description = 'Фото'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'