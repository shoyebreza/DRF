from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer

# Create your views here.


@api_view()
def view_products(request):
    product = Product.objects.select_related('category').all()
    serializer = ProductSerializer(product, many=True, context = {'request': request})
    return Response(serializer.data)






@api_view()
def view_specific_products(request, id):
    product = get_object_or_404(Product, pk=id)

    #product_dict = {'id': product.id, 'name': product.name, 'price': product.price}
    #return Response(product_dict)

    serializer = ProductSerializer(product)
    return Response(serializer.data)

    # method 1-----------------
    # try:
    #     product = Product.objects.get(pk=id)
    #     product_dict = {'id': product.id, 'name': product.name, 'price': product.price}
    #     return Response(product_dict)
    # except Product.DoesNotExist:
    #     return Response({"message" : "does not exist "}, status = status.HTTP_404_NOT_FOUND)



@api_view()
def view_categories(request):
    return Response({"message": "category"})


@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)








