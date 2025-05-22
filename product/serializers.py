from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'price', 'stock',
            'sku', 'image', 'date_added', 'category', 'is_deleted'
        ]
        read_only_fields = ['id', 'date_added', 'is_deleted']