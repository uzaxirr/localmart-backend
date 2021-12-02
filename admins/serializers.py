"""Serialize all Models Here"""
from rest_framework import serializers
from .models import GeometryModel, ProperitesModel, ProductModel, InventoryModel, StoreModel, OrdersModel

class GeometrySerializer(serializers.ModelSerializer):
    """Serializer class For geometry Model"""
    class Meta:
        """Serialize All feilds"""
        model = GeometryModel
        fields = '__all__'

class ProperitesSerializer(serializers.ModelSerializer):
    """Serializer class For properties Model"""
    class Meta:
        """Serialize All feilds"""
        model = ProperitesModel
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """Serializer class For product Model"""
    class Meta:
        """Serialize All feilds"""
        model = ProductModel
        fields = '__all__'

class InventorySerializer(serializers.ModelSerializer):
    """Serializer class For inventory Model"""
    class Meta:
        """Serialize All feilds"""
        model = InventoryModel
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    """Serializer class For store Model"""
    class Meta:
        """Serialize All feilds"""
        model = StoreModel
        fields = '__all__'

class AllStoreSerializer(serializers.ModelSerializer):
    """Serializer class For store Model"""
    geometry = GeometrySerializer(many=True, read_only=True)
    class Meta:
        """Serialize All feilds"""
        model = StoreModel
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    """Serializer class For order Model"""
    class Meta:
        """Serialize All feilds"""
        model = OrdersModel
        fields = '__all__'
        