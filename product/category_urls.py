

from django.urls import path
from product import views






urlpatterns = [
    path('', views.ViewCategories.as_view(), name='category-list'),
    #path('<int:id>/', views.ViewSpecificCategory.as_view(), name='view_specific_category'),
    path('<int:pk>/', views.CategoryDetails.as_view(), name='view_specific_category'),  
]
