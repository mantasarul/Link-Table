from django.urls.conf import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add-category', views.AddCategoryView.as_view(), name="add-category"),
    path('add-link', views.AddLinkView.as_view(), name="add-link"),
    path('all-categories', views.AllCategoriesView.as_view(), name='all-categories'),
    path('all-links', views.AllLinksView.as_view(), name='all-links'),
    path('delete-category/<int:pk>', views.DeleteCategoryView.as_view(), name='delete-category'),
    path('edit-category/<pk>', views.EditCategoryView.as_view(), name='update-category'),
    path('delete-link/<int:pk>', views.DeleteLinkView.as_view(), name='delete-link'),
    path('edit-link/<pk>', views.EditLinkView.as_view(), name='update-link'),
    # path('delete-category/<int:id>', views.deleteCategory),
    # path('edit-category/<int:id>', views.editCategory),
    # path('<pk>/update', views.EditCategoryView.as_view(), name='update-category'),
    # path('edit-link/<int:id>', views.editLink),
]

# <-- Update View Routing -->
# from django.urls import path
	
# # importing views from views..py
# from .views import GeeksUpdateView
# urlpatterns = [
# 	# <pk> is identification for id field,
# 	# <slug> can also be used
# 	path('<pk>/update', GeeksUpdateView.as_view()),
# ]


# <-- Delete View Routing -->
# from django.urls import path
 
# # importing views from views..py
# from .views import GeeksDeleteView
# urlpatterns = [
#     # <pk> is identification for id field,
#     # slug can also be used
#     path('<pk>/delete/', GeeksDeleteView.as_view()),
# ]