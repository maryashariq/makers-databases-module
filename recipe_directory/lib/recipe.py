class Recipe:
    def __init__(self, id, recipe_name, avg_cooking_time, rating):
        self.id = id
        self.recipe_name = recipe_name
        self.avg_cooking_time = avg_cooking_time
        self.rating = rating
    
    def __eq__(self, other):
        return self.id == other.id
        return self.recipe_name == other.recipe_name
        return self.avg_cooking_time == other.avg_cooking_time
        return self.rating == other.rating
    
    def __repr__(self):
        return f"Recipe({self.id}, {self.recipe_name}, {self.avg_cooking_time}, {self.rating})"
    