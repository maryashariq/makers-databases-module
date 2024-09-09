from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Artist objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/recipes_seeds.sql") 
    repository = RecipeRepository(db_connection)

    recipes = repository.all() # 

    # Assert on the results
    assert recipes == [
        Recipe(1, "Sushi", 40, 5),
        Recipe(2, "Udon", 15, 4),
        Recipe(3, "Kebab", 45, 4),
        Recipe(4, "Spanakopita", 60, 5)
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipes_seeds.sql") 
    repository = RecipeRepository(db_connection)

    recipe = repository.find(1)
    assert recipe == Recipe(1, "Sushi", 40, 5)

"""
When we call ArtistRepository#create
We get a new record in the database.
"""
# def test_create_record(db_connection):
#     db_connection.seed("seeds/recipe_seeds.sql") 
#     repository = RecipeRepository(db_connection)

#     repository.create(Artist(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(3, "Taylor Swift", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#         Artist(5, "The Beatles", "Rock"),
#     ]

