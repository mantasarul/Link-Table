from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView

from .forms import AddLinkForm, CategoryForm
from .models import Category, Link

# Create your views here.

class HomeView(TemplateView):
    template_name = 'table_app/home.html'


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'table_app/add-category.html'
    success_url = 'all-categories'


# class AddCategoryView(FormView):
#     template_name = 'table_app/add-category.html'
#     form_class = CategoryForm
#     success_url = '/all-categories'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# class AddCategoryView(View):
#     def get(self, request):
#         form = CategoryForm()

#         return render(request, 'table_app/add-category.html', {
#             'form': form
#         })

#     def post(self, request):
#         form = CategoryForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')

#         return render(request, 'table_app/add-category.html', {
#             'form': form
#         })


class AddLinkView(CreateView):
    model = Link
    form_class = AddLinkForm
    template_name = 'table_app/add-link.html'
    success_url = 'all-links'


class AllCategoriesView(ListView):
    template_name = 'table_app/view-categories.html'
    model = Category


class AllLinksView(ListView):
    template_name = 'table_app/view-links.html'
    model = Link