from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    # explain
    # queryset: This is the set of items that will be used to populate the viewset.
    # The queryset is set to all items in the database.
    # serializer_class: This is the serializer class that will be used to convert the Item model instances to and from JSON.
    # The serializer class is set to ItemSerializer, which is defined in the serializers.py file.
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
