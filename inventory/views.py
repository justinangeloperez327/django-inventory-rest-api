from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .models import Category
from .models import Supplier
from .models import StockMovement
from .models import Location
from .serializers import ItemSerializer
from .serializers import CategorySerializer
from .serializers import SupplierSerializer
from .serializers import StockMovementSerializer
from .serializers import LocationSerializer

class ItemViewSet(viewsets.ModelViewSet):
    # explain
    # queryset: This is the set of items that will be used to populate the viewset.
    # The queryset is set to all items in the database.
    # serializer_class: This is the serializer class that will be used to convert the Item model instances to and from JSON.
    # The serializer class is set to ItemSerializer, which is defined in the serializers.py file.
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    

class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer