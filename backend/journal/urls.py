from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, ExperimentViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'experiments', ExperimentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
