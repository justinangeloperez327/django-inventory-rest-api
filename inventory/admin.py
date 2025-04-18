from django.contrib import admin
from .models import Item
from .models import Category
from .models import Supplier
from .models import StockMovement
from .models import Location

# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('category', 'supplier', 'created_at')
    ordering = ('-created_at',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)
    
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    
@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'movement_type', 'timestamp')
    search_fields = ('item__name',)
    list_filter = ('movement_type',)
    ordering = ('-timestamp',)
    

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    ordering = ('name',)