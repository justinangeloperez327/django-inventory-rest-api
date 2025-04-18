from rest_framework import serializers
from .models import Item, Category, Supplier, StockMovement, Location

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        
class StockMovementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockMovement
        fields = '__all__'
    
    def create(self, validated_data):
        # Extract the item and quantity from the validated data
        item = validated_data.get('item')
        quantity = validated_data.get('quantity')
        movement_type = validated_data.get('movement_type')

        # Update the item's quantity based on the movement type
        if movement_type == 'IN':  # Stock In
            item.quantity += quantity
        elif movement_type == 'OUT':  # Stock Out
            if item.quantity >= quantity:
                item.quantity -= quantity
            else:
                raise serializers.ValidationError("Not enough stock to complete this operation.")

        # Save the updated item
        item.save()

        # Create and return the StockMovement instance
        return super().create(validated_data)
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'