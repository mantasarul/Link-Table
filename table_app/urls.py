from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('add-category', views.AddCategoryView.as_view()),
    path('add-link', views.AddLinkView.as_view()),
    path('all-categories', views.AllCategoriesView.as_view()),
    path('all-links', views.AllLinksView.as_view()),    

]
