from django.shortcuts import render
from rest_framework import viewsets
from pantry import serializers
from core.models import Pantry, IngredientType, Ingredient
from rest_framework import authentication, permissions

class PantryViewSet(viewsets.ModelViewSet):
    queryset = Pantry.objects.all()
    serializer_class = serializers.PantrySerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user_id = self.request.user)

    def perform_create(self, serializer):
        try: 
            serializer.save(user=self.request.user)
        except:
            raise ValueError("ユーザー名は必須です")