from django.urls import path
from .views import *
urlpatterns = [
    path('categories',ListCategory.as_view(),name='categorie'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='singlecategorie'),
    path('books',ListBook.as_view(),name='books'),
    path('books/<int:pk>/',DetailBook.as_view(),name='singlebooks'),
    path('product',ListProduct.as_view(),name='product'),
    path('product/<int:pk>/',DetailProduct.as_view(),name='singleproduct'),





]
