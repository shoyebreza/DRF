from django.urls import path,include
from product.views import ProductViewSet, CategoryViewSet,RewiewViewSet
from order.views import CartViewSet,CartItemViewset
from rest_framework_nested import routers



# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet)
router.register('carts', CartViewSet, basename='carts')




product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', RewiewViewSet, basename='product-review')
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', CartItemViewset, basename='cart-item')

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
    path('',include(cart_router.urls)),
]




