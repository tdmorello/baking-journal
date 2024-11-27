from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Experiment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    notes = models.TextField()
    outcome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe.title} - {self.outcome}"
