
## 1. Extract nouns from the user stories or specification

```
As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep a list of all my recipes with their names.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to keep the average cooking time (in minutes) for each recipe.

As a food lover,
So I can stay organised and decide what to cook,
I'd like to give a rating to each of the recipes (from 1 to 5).

```

```
Nouns:

recipe, recipe_name, avg_cooking_time, rating
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------- |
| recipe                | recipe_name, avg_cooking_time, rating |

Name of the table (always plural): `recipes`

Column names: `recipe_name`, `avg_cooking_time`, `rating`

## 3. Decide the column types

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

id: SERIAL
recipe_name: text
avg_cooking_time: int
rating: int
```

## 4. Write the SQL

```sql
-- EXAMPLE
-- file: albums_table.sql

-- Replace the table name, column names and types.

CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  recipe_name text,
  avg_cooking_time int,
  rating int
);
```

## 5. Create the table

```bash
psql -h 127.0.0.1 my_recipes < recipes_seeds.sql
```