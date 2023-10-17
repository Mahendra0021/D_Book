from rest_framework import serializers
from .models import Category, Book,Product
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        fields=('id','title')
        model=Category

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'title',
            'category',
            'isbn',
            'pages',
            'price',
            'stock',
            'description',
            'imageUrl',
            'status',
            'date_created',
            )
        model=Book

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'Product_tag',
            'name',
            'category',
            'price',
            'stock',
            'imageUrl',
            'status',
            'date_created',
            )
        model=Product


