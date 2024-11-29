from journal.models import Recipe, Experiment

def populate_data():
    # Create Recipes
    recipes = [
        Recipe(
            title="Classic Chocolate Chip Cookies",
            ingredients="2 1/4 cups flour, 1 tsp baking soda, 1 tsp salt, 1 cup butter, 3/4 cup sugar, 3/4 cup brown sugar, 1 tsp vanilla extract, 2 large eggs, 2 cups chocolate chips",
            instructions="Preheat oven to 375°F. Mix dry ingredients in one bowl. Cream butter and sugars, add vanilla and eggs. Gradually blend in dry ingredients. Stir in chocolate chips. Drop by rounded tablespoons onto ungreased baking sheets. Bake 9-11 minutes."
        ),
        Recipe(
            title="Rustic Sourdough Bread",
            ingredients="500g bread flour, 350g water, 100g sourdough starter, 10g salt",
            instructions="Mix all ingredients. Rest for 30 minutes. Stretch and fold the dough every 30 minutes for 2 hours. Shape and let proof overnight in the fridge. Bake at 475°F in a preheated Dutch oven for 30 minutes covered, then 15 minutes uncovered."
        )
    ]
    Recipe.objects.bulk_create(recipes)

    # Create Experiments
    experiments = [
        Experiment(
            recipe=Recipe.objects.get(title="Classic Chocolate Chip Cookies"),
            notes="Reduced sugar by 10%. Cookies were less sweet but still tasty.",
            outcome="Good",
            created_at="2024-11-26"
        ),
        Experiment(
            recipe=Recipe.objects.get(title="Rustic Sourdough Bread"),
            notes="Increased hydration to 75%. Bread was more airy but harder to shape.",
            outcome="Great",
            created_at="2024-11-27"
        )
    ]
    Experiment.objects.bulk_create(experiments)

populate_data()
