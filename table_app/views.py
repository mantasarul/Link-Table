from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, FormView, UpdateView
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


# def deleteCategory(request, id):
#     category = Category.objects.get(id=id)
#     category.delete()
#     return redirect("/all-categories")


class DeleteCategoryView(View):
    def get(self, request, id):
        category = Category.objects.get(id=id)
        return render(request, 'table_app/delete-category.html', {
            # 'id': id
            'category': category.category_name

        })

    def post(self, request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect('/all-categories')


class DeleteLinkView(View):
    def get(self, request, id):
        link = Link.objects.get(id=id)
        return render(request, 'table_app/delete-link.html', {
            # 'id':id
            'link': link.link_name
        })

    def post(self, request, id):
        link = Link.objects.get(id=id)
        link.delete()
        return HttpResponseRedirect('/all-links')


# def editCategory(request, id):
#     instance = get_object_or_404(Category, id=id)
#     form = CategoryForm(request.POST or None, instance=instance)

#     if form.is_valid():
#         form.save()
#         return redirect("/all-categories")

#     return render(request, 'table_app/add-category.html', {
#         'form': form
#     })


class EditCategoryView(UpdateView):
    model = Category
    template_name = 'table_app/edit-category.html'
    fields = ['category_name']
    success_url = '/all-categories'


# class EditCategoryView(View):
#     def get(self, request, id):
#         instance = get_object_or_404(Category, id=id)
#         form = CategoryForm(request.POST or None, instance=instance)

#         return render(request, 'table_app/edit-category.html', {
#             'form': form
#         })

#     def post(self, request, id):
#         instance = get_object_or_404(CategoryForm, id=id)
#         form = CategoryForm(request.POST or None, instance=instance)
        
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/all-categories")

#         return render(request, 'table_app/add-category.html', {
#             'form': form
#         })


def editLink(request, id):
    instance = get_object_or_404(Link, id=id)
    form = AddLinkForm(request.POST or None, instance=instance)

    if form.is_valid():
        form.save()
        return redirect("/all-links")

    return render(request, 'table_app/add-link.html', {
        'form': form
    })