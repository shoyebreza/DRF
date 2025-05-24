from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count

# Create your views here.


@api_view(['GET','POST'])
def view_products(request):
    if request.method == 'GET':
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializer(product, many=True, context = {'request': request})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)

        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status = status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)



    






@api_view(['GET','PUT','DELETE'])
def view_specific_products(request, id):
    if request.method =='GET':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    if request.method =='DELETE':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




        
    #product_dict = {'id': product.id, 'name': product.name, 'price': product.price}
    #return Response(product_dict)

    # method 1-----------------
    # try:
    #     product = Product.objects.get(pk=id)
    #     product_dict = {'id': product.id, 'name': product.name, 'price': product.price}
    #     return Response(product_dict)
    # except Product.DoesNotExist:
    #     return Response({"message" : "does not exist "}, status = status.HTTP_404_NOT_FOUND)



@api_view()
def view_categories(request):
    categories = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)








