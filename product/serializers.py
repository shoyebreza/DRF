from rest_framework import serializers
from decimal import Decimal
from product.models import Category #, Product, Review, ProductImage
# from django.contrib.auth import get_user_model



class CategorySerializer(serializers.Serializer):
    id= serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()





class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name =  serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset = Category.objects.all()
    # )
    #category = serializers.StringRelatedField()
    #category = CategorySerializer()

    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(), view_name = 'view_specific_category'
    )



    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1),2)