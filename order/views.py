from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin , RetrieveModelMixin, DestroyModelMixin
from order.models import Cart, CartItem, Order, OrderItem
from order.serializers import CartSerializer, CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer,OrderSerializer,UpdateOrderSerializer,CreateOrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Cart.objects.none()
        return Cart.objects.prefetch_related('items__product').filter(user=self.request.user)


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if getattr(self, 'swagger_fake_view', False):
            return context

        return {'cart_id': self.kwargs.get('cart_pk')}

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs.get('cart_pk'))
    



class OrderViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'patch', 'head', 'options']

    def get_permissions(self):
        if self.request.method in ['PATCH','DELETE']:
            return [IsAdminUser()]
        return [IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer

    def get_serializer_context(self):
        return {'user_id': self.request.user.id, 'user': self.request.user.id}

    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.prefetch_related('items__product').all()
        return Order.objects.prefetch_related('items__product').filter(user=self.request.user)