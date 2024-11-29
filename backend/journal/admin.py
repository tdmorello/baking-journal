from django.contrib import admin
from .models import Recipe, Experiment

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Fields to display in the list view
    search_fields = ('title',)             # Add a search bar for these fields
    list_filter = ('created_at',)         # Add filters for these fields

class ExperimentAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'outcome', 'created_at')
    search_fields = ('notes', 'outcome')
    list_filter = ('created_at',)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Experiment, ExperimentAdmin)

# # Or make the experiments inline and associated with recipes by using the following instead
# class ExperimentInline(admin.TabularInline):  # Or use StackedInline for a vertical layout
#     model = Experiment

# class RecipeAdmin(admin.ModelAdmin):
#     inlines = [ExperimentInline]

# admin.site.register(Recipe, RecipeAdmin)
