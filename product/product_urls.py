

from django.urls import path
from product import views






urlpatterns = [
    #path('', views.view_products, name='product-list'),
    path('', views.ViewProducts.as_view(), name='product-list'),
    #path('<int:id>/', views.view_specific_products, name='product-list'),
    path('<int:id>/', views.ViewSpecificProduct.as_view(), name='product-list'),
]
