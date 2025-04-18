from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from .views import CategoryViewSet
from .views import SupplierViewSet
from .views import StockMovementViewSet
from .views import LocationViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'stock_movements', StockMovementViewSet, basename='stockmovement')
router.register(r'locations', LocationViewSet, basename='location')

urlpatterns = [
    path('', include(router.urls)),
]