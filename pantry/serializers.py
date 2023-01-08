from rest_framework import serializers
from core.models import Pantry, IngredientType, Ingredient

class PantrySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d", read_only=True)

    class Meta:
        model = Pantry
        fields = ('id', 'name', 'user_id', 'created_at', 'updated_at')
        extra_kwargs = {'user_id': {'read_only': True}}
