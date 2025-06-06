from rest_framework import serializers
from decimal import Decimal
from product.models import Category , Product , Review #, ProductImage
# from django.contrib.auth import get_user_model



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','description', 'product_count']

    product_count =  serializers.IntegerField(read_only=True)

    # product_count = serializers.SerializerMethodField(
    #     method_name='get_product_count'
    # )

    # def get_product_count(self, category):
    #     count = Product.objects.filter(category=category).count()
    #     return count

    
# class CategorySerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()





# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name =  serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
#     price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
#     # category = serializers.PrimaryKeyRelatedField(
#     #     queryset = Category.objects.all()
#     # )
#     #category = serializers.StringRelatedField()
#     #category = CategorySerializer()

#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(), view_name = 'view_specific_category'
#     )

#     def calculate_tax(self, product):
#         return round(product.price * Decimal(1.1),2)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'

        fields = ['id','name','description','price','stock','category','price_with_tax']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(), view_name = 'view_specific_category'
    # )
    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    def validate_price(self, price):
        if price <0:
            raise serializers.ValidationError('price could not be nagative')
        return price
    
    # ------object label validation -----------
    # def create(self, validated_data):
    #     product = Product(**validated_data)
    #     product.other =1
    #     product.save()
    #     return product
    
    # ----------field validation ------------------
    # def validate(self, attrs):
    #     if attrs['password1'] != attrs['password2']:
    #         raise serializers.ValidationError("Password didn't match")



class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review