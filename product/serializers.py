from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "stock",
            "get_image",
            "get_thumbnail"
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "stock"
        )
    
    def update(self, instance, validated_data):
        """
        Update and return an existing `stock` instance, given the validated data.
        """
        instance.stock = validated_data.get('stock', instance.stock)
        instance.save()
        return instance