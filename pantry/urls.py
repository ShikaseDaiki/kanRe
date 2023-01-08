from django.urls import path, include
from rest_framework.routers import DefaultRouter
from pantry import views

app_name = 'pantry'

router = DefaultRouter()
router.register('pantry', views.PantryViewSet)

urlpatterns = [
    path('', include(router.urls))
]