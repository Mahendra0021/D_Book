from django.shortcuts import render
from .serializers import CategorySerializers,BookSerializers,ProductSerializers
from .models import Category,Book,Product
from rest_framework import generics


class ListCategory(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers

class DetailCategory(generics.RetrieveDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers

class ListBook(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializers

class DetailBook(generics.RetrieveDestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializers

class ListProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    
class DetailProduct(generics.RetrieveDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

