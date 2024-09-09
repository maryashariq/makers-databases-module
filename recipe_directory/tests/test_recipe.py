from lib.recipe import Recipe

"""
Recipe constructs with an id, name and genre
"""
def test_recipe_constructs():
    recipe = Recipe(1, "Test Recipe", 30, 5)
    assert recipe.id == 1
    assert recipe.recipe_name == "Test Recipe"
    assert recipe.avg_cooking_time == 30
    assert recipe.rating == 5

"""
We can format artists to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Test Recipe", 30, 5)
    assert str(recipe) == "Recipe(1, Test Recipe, 30, 5)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical artists
And have them be equal
"""
def test_artists_are_equal():
    recipe1 = Recipe(1, "Test Recipe", 30, 5)
    recipe2 = Recipe(1, "Test Recipe", 30, 5)

    assert recipe1 == recipe2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
