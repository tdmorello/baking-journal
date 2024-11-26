from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class JournalEntry(models.Model):
    title = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipe, related_name='entries', on_delete=models.CASCADE)
