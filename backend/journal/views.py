"""
Used by djangorestframework to handle CRUD operations.
"""

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Recipe, Experiment
from .serializers import RecipeSerializer, ExperimentSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(detail=False, methods=["get"])
    def recent(self, request):
        recent_recipes = self.queryset.order_by("-created_at")[:5]
        serializer = self.get_serializer(recent_recipes, many=True)
        return Response(serializer.data)


class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer

    @action(detail=False, methods=["get"])
    def recent(self, request):
        recent_recipes = self.queryset.order_by("-created_at")[:5]
        serializer = self.get_serializer(recent_recipes, many=True)
        return Response(serializer.data)
