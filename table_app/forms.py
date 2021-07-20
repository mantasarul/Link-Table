from django.forms import fields, widgets
from table_app.models import Category, Link
from django import forms

class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'category_name': 'Category Name'
        }
        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AddLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        labels = {
            'link_name': 'Link',
            'category_id': 'Category ID'
        }
        widgets = {
            'link_name': forms.TextInput(attrs={'class': 'form-control'}),
            'category_id': forms.Select(attrs={'class': 'form-control'}),
        }