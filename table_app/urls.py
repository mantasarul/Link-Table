from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('add-category', views.AddCategoryView.as_view(), name="add-category"),
    path('add-link', views.AddLinkView.as_view(), name="add-link"),
    path('all-categories', views.AllCategoriesView.as_view(), name='all-categories'),
    path('all-links', views.AllLinksView.as_view(), name='all-links'),
    # path('delete-category/<int:id>', views.deleteCategory),
    path('delete-category/<int:id>', views.DeleteCategoryView.as_view()),
    path('edit-category/<int:id>', views.editCategory),
    # path('edit-category/<int:id>', views.EditCategoryView.as_view()),
    path('delete-link/<int:id>', views.DeleteLinkView.as_view()),
    path('edit-link/<int:id>', views.editLink),


]
