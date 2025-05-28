from django.urls import path,include
from product.views import ProductViewSet, CategoryViewSet,RewiewViewSet
from rest_framework_nested import routers



# router = SimpleRouter()
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('categories', CategoryViewSet)
product_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
product_router.register('reviews', RewiewViewSet, basename='product-review')


#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
]




