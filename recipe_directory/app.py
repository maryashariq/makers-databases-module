from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipes_seeds.sql")

# Retrieve all artists
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

# List them out
for recipe in recipes:
    print(recipe)

# Get one row from recipes table

print(recipe_repository.find(1))