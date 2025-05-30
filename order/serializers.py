from rest_framework import serializers
from order.models import Cart, CartItem
from product.serializers import ProductSerializer




class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    product_price = serializers.SerializerMethodField(method_name='get_product_price')
    class Meta:
        model = CartItem
        fields = ['id','product','quantity','product_price']

    def get_product_price(self,cart_item):
        return cart_item.product.price





class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['id','user','items']





