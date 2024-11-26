from django.urls import path
from .views import RecipeList, JournalEntryList

urlpatterns = [
    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('entries/', JournalEntryList.as_view(), name='journal-entry-list'),
]
