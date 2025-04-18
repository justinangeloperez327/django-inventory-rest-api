from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='items')
    supplier = models.ForeignKey('Supplier', on_delete=models.SET_NULL, null=True, related_name='items')
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    barcode = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_discontinued = models.BooleanField(default=False)
    reorder_level = models.PositiveIntegerField(default=0)
    reorder_quantity = models.PositiveIntegerField(default=0)
    min_order_quantity = models.PositiveIntegerField(default=0)
    max_order_quantity = models.PositiveIntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        db_table = 'inventory_items'
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
        indexes = [
            models.Index(fields=['name']),
        ]

        
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'inventory_categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_info = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inventory_suppliers'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name

class StockMovement(models.Model):
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='stock_movements')
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=50, choices=[('IN', 'Stock In'), ('OUT', 'Stock Out')])
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inventory_stock_movements'
        verbose_name = 'Stock Movement'
        verbose_name_plural = 'Stock Movements'

    def __str__(self):
        return f"{self.movement_type} - {self.item.name} ({self.quantity})"

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'inventory_locations'
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name