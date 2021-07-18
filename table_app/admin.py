from django.contrib import admin
from .models import Category, Link

# Register your models here.

class CategoryModel(admin.ModelAdmin):
    list_display = ('id', 'category_name')

    class Meta:
        verbose_name_plural = 'Categories'


class LinkModel(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'link_name')

    class Meta:
        verbose_name_plural = 'Links'


admin.site.register(Category, CategoryModel)
admin.site.register(Link, LinkModel)