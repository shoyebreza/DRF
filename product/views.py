from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer, ReviewSerializers
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter,OrderingFilter
#from rest_framework.pagination import PageNumberPagination
from product.paginations import DefaultPagination
#from rest_framework.permissions import IsAdminUser, AllowAny
from api.permissions import IsAdminOrReadOnly, FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthorOrReadonly

# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends= [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    #pagination_class = PageNumberPagination
    pagination_class = DefaultPagination
    search_fields = ['name', 'description','category__name']
    ordering_fields = ['price','updated_at']
    #permission_classes = [IsAdminUser]
    permission_classes = [IsAdminOrReadOnly]
    #permission_classes = [DjangoModelPermissions]
    #permission_classes = [FullDjangoModelPermission]
    #permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    #filterset_fields = ['category_id','price']


    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     return [IsAdminUser()]


    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     category_id = self.request.query_params.get('category_id')
    #     if category_id is not None:
    #         queryset = Product.objects.filter(category_id=category_id)
    #     return queryset

    def destroy(self, request, *args, **kwargs):
        product  = self.get_object()
        if product.stock > 10:
            return Response({'message': 'product can not delete with stock'})
        self.perform_destroy(product)
        return Response(status = status.HTTP_204_NO_CONTENT)
    


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer




# -----------function base api view -----------------

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


# --------- class based api view ----------------

class ViewProducts(APIView):
    def get(self, request):
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializer(product, many=True, context = {'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception= True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    

# mixins ------------------- Generic view-----

class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer


    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer
    
    # def get_serializer_context(self):
    #     return {'request': self.request}



class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # method overriding--------

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.stock > 10:
            return Response({'message': 'product can not delete with stock'})
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# function based 
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


# class based

class ViewSpecificProduct(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
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

class ViewCategories(APIView):
    def get(self, request):
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer

@api_view()
def view_specific_category(request,pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)


class ViewSpecificCategory(APIView):
    def get(self, request, id):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=id)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, id):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=id)
        serializer = CategorySerializer(category, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')).all(), pk=id)
        category.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)




class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadonly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}


