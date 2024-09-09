# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](./single_table_design_recipe_template.md).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: movies

Columns:
id | title | release_year | director_id
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql

-- file: movies_library_seed_demo.sql

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE movies RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO movies (title, release_year, director_id) VALUES ('Challengers', 2024, 1);
INSERT INTO movies (title, release_year, director_id) VALUES ('American Fiction', 2024, 2);
INSERT INTO movies (title, release_year, director_id) VALUES ('Boogie Nights', 1997, 3);
INSERT INTO movies (title, release_year, director_id) VALUES ('Argentina 1985', 2023, 4);
INSERT INTO movies (title, release_year, director_id) VALUES ('Poor Things', 2023, 5);
INSERT INTO movies (title, release_year, director_id) VALUES ('The Holdovers', 2023, 6);
INSERT INTO movies (title, release_year, director_id) VALUES ('BlackBerry', 2023, 7);
INSERT INTO movies (title, release_year, director_id) VALUES ('Licorice Pizza', 2021, 3)

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 movies_library < movies_library_seed_demo.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)
class Movie


# Repository class
# (in lib/student_repository.py)
class MovieRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Movie:
    def __init__(self, id, title, release_year, director_id):
        self.id = 0
        self.title = ""
        self.release_year = 0000
        self.director_id = 0

# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> movie = Movie()
# >>> movie.title = "Challengers"
# >>> movie.release_year = 2024
# >>> movie.director_id = 1
# ''
# >>> movies.title
# 'Challengers'

```

*You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.*

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: movies

# Repository class
# (in movies_repository.py)

class MovieRepository():

    # Selecting all records
    # No arguments
    def all(self):
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM movies;

        # Returns an array of Movie objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(self, id):
        #Arguments: 
        #   Movie ID represented as int
        # Executes the SQL query:
        # SELECT id, title, release_year, director_id FROM movies WHERE id = movie.id

        # Returns a single Movie object.

        # Add more methods below for each operation you'd like to implement.

    def create(self, movie):
    # Executes the SQL query:
    # INSERT INTO movies (title, release_year, artist_id) VALUES (%s, %s, %s), [movie.title, movie.release_year, movie.artist_id])

    # Example:
    # INSERT INTO movies (title, release_year, artist_id) VALUES ('American Fiction', 2024, 2)

    # Returns None 
    #Side effects: Inserts new row/record into movies table in movie_library db

    def update(self, id)
    #Arguments:
        # ID = movie id represented as int
    # Executes the SQL query:
    # UPDATE movies SET [column_name] = [new_value] WHERE id = [id]
    # 

    #Returns None
    # Side effects: updates value in the specified column for specified movie id

    def delete(self, id):
        # Arguments:
    #       Movie ID represented as int
    # Executes the SQL query:
    # DELETE FROM movies WHERE id = %s, [id]

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python

repo = MovieRepository()

movies = repo.all()

len(movies) # =>  8

movies[0].id # =>  1
movies[0].title # => 'Challengers'
movies[0].release_year # => 2024
movies[0].director_id # => 1

movie[1].id # =>  2
movie[1].title # => 'American Fiction'
movie[1].release_year # => 2024
movie[1].director_id # => 2

# 2
# Get a single student

repo = MovieRepository()

movie = repo.find(3)

movie.id # =>  3
movie.title # => 'Boogie Nights'
movie.release_year # => 1997
movie.artist_id # => 3

# Add more examples for each method
```

Encode this example as a test.

# Test get a single record 
```python

def test_retrieve_single_record_from_id():
    repo = MovieRepository()
    result = repo.find(1)
    assert result == Movie(1, 'Challengers', 2024, 1)


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._