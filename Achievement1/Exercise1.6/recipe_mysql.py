# initialize mySQL
import mysql.connector

# initialize connection to mySQL
conn = mysql.connector.connect(
    host='localhost',
    user='cf-python',
    passwd='password')
cursor = conn.cursor()

def create_DB_table(conn, cursor):
  # initialize DB
  cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
  cursor.execute("USE task_database")

  # create table
  cursor.execute('''CREATE TABLE IF NOT EXISTS recipes(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                ingredients VARCHAR(250),
                cooking_time INT,
                difficulty VARCHAR(20)
                )''')
  conn.commit()


def main_menu(conn, cursor):
  # main menu display + all mySQL functions

  def calculate_difficulty(cooking_time, ingredients):
       # calculate the difficulty based on two provided arguments
       if cooking_time < 10 and len(ingredients) < 4:
         difficulty = "Easy"
       elif cooking_time < 10 and len(ingredients) >= 4:
         difficulty = "Medium"
       elif cooking_time >= 10 and len(ingredients) < 4:
         difficulty = "Intermediate"
       elif cooking_time >= 10 and len(ingredients) >= 4:
         difficulty = "Hard"
       return difficulty

  # operations 
  # -----------------------------------------------------------------------------------------  
  def create_recipe(): 
    # Create a recipe to be stored in your recipes database
    # intake data for new recipe
    print("Create a new Recipe to submit! ------------")
    name = input("Recipe name: ")
    cooking_time = int(input("Cooking-time (min): "))
    ingredients = input("Ingredients (separate with comma): ").split(', ')
    ingredients_str = ", ".join(ingredients)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    
    # query new recipe into table
    create_query = "INSERT INTO recipes (name, cooking_time, ingredients, difficulty) VALUES (%s, %s, %s, %s)"
    cursor.execute(create_query, (name, cooking_time, ingredients_str, difficulty))
    conn.commit()
    print("Recipe added!")
    print()
  
  # -----------------------------------------------------------------------------------------  
  def search_recipe():
    # search through recipes in your DB by ingredients
    # retrieve all ingredients from recipes table
    cursor.execute("SELECT ingredients FROM recipes")
    results = cursor.fetchall()
    all_ingredients = []
    for row in results:
      ingredients = row[0].split(', ')
      for item in ingredients:
        if item not in all_ingredients:
          all_ingredients.append(item)

    # display all ingredients
    print("All Ingredients")
    print("--------------------")
    for item, value in enumerate(all_ingredients):
        print(str(item) + " " + str(value))
    search_number = int(input("Choose the number of the ingredient you would like to search: "))
    search_ingredient = all_ingredients[search_number]

    # query recipe based on search_ingredient
    search_query = ("SELECT * FROM recipes WHERE ingredients LIKE %s")
    cursor.execute(search_query, ('%' + search_ingredient + '%',)) # added a comma here to make a tuple 
    # display result
    recipes = cursor.fetchall()
    if recipes:
      print("Recipes with a match!")
      print("------------------")
      for row in recipes:
        print("ID: ", row[0])
        print("Name: ", row[1])
        print("Cooking-time: ", row[2])
        print("Ingredients: ", row[3])
        print("Difficulty: ", row[4])
        print()
    else:
      print("Sorry no matches")
  
  # -----------------------------------------------------------------------------------------  
  def update_recipe():
    # update a selected recipe (name, cooking_time, ingredients)
    # retrieve and display all recipes in table
    cursor.execute("SELECT id, name, cooking_time, ingredients, difficulty FROM recipes")
    results = cursor.fetchall()
    print("All Recipes")
    print("--------------------")
    print()
    for row in results:
      print("ID: ", row[0])
      print("Name: ", row[1])
      print("Cooking-time: ", row[2])
      print("Ingredients: ", row[3])
      print("Difficulty: ", row[4])
      print()

    # selection inputs
    choice_recipe = int(input("Select the ID of the recipe you'd like to update: "))
    choice_column = input("What column (Name, Cooking-time, Ingredients) would you like to update? ")

    # applying inputs
    if choice_column == "Name":
      choice_value = input("Input the new Name: ")
      # add new value
      update_query = "UPDATE recipes SET name = %s WHERE id = %s"
      cursor.execute(update_query, (choice_value, choice_recipe))
      conn.commit()

    elif choice_column == "Cooking-time":
      choice_value = input("Input the new cooking-time: ")
      # add new value
      update_query = "UPDATE recipes SET cooking_time = %s WHERE id = %s"
      cursor.execute(update_query, (choice_value, choice_recipe))
      conn.commit()

    elif choice_column == "Ingredients":
      choice_value = input("Input the new ingredients (separate with comma): ")
      # add new value
      update_query = "UPDATE recipes SET ingredients = %s WHERE id = %s"
      cursor.execute(update_query, (choice_value, choice_recipe))
      conn.commit()

    if choice_column == "Cooking-time" or "Ingredients":
      # update difficulty
      # retrieve new updated values
      cursor.execute("SELECT cooking_time, ingredients FROM recipes WHERE id = %s", (choice_recipe,))# added comma to make tuple, must be tuple, dict, or list
      new_values = cursor.fetchone()
      if new_values:
        cooking_time = new_values[0]
        ingredients = new_values[1]
        # covert ingredient value into list 
        ingredient_list = ingredients.split(', ')
        # calculate with new values
        difficulty = calculate_difficulty(cooking_time, ingredient_list)
        # query new difficulty value
        update_difficulty_query = "UPDATE recipes SET difficulty = %s WHERE id = %s"
        cursor.execute(update_difficulty_query, (difficulty, choice_recipe))
        conn.commit()
      else:
        print("No recipe found with that ID (-> difficulty update/check)")
  
  # -----------------------------------------------------------------------------------------  
  def delete_recipe():
    # delete a selected recipe
    # retrieve and display all recipes in table
    cursor.execute("SELECT id, name, cooking_time, ingredients, difficulty FROM recipes")
    results = cursor.fetchall()
    print("All Recipes")
    print("--------------------")
    print()
    for row in results:
      print("ID: ", row[0])
      print("Name: ", row[1])
      print("Cooking-time: ", row[2])
      print("Ingredients: ", row[3])
      print("DIfficulty: ", row[4])
      print()
    
    # selection input and confirmation
    choice_recipe = int(input("Select the ID of the recipe you'd like to delete: "))
    confirm_delete = input("Are you sure you want to delete recipe: ID-" + str(choice_recipe) + " ? y/n: ")
    # query delete
    if confirm_delete == 'y':
      delete_query = "DELETE FROM recipes WHERE id = %s"
      cursor.execute(delete_query, (choice_recipe,))
      conn.commit()
    else:
      print("Be more decisive next time.") 

  # -----------------------------------------------------------------------------------------  
  # display loop
  choice = None
  while(choice != 'quit'):
    print("Main Menu")
    print("--------------------")
    print("Pick a choice: ")
    print("  1. Create a new recipe")
    print("  2. Search for a recipe by ingredient")
    print("  3. Update an existing recipe")
    print("  4. Delete a recipe")
    print("  Type 'quit' to exit the program")
    print("---------------------")
    choice = input("Your choice (enter a number or quit): ")

    if choice == '1':
      create_recipe()
    elif choice =='2':
      search_recipe()
    elif choice == '3':
      update_recipe()
    elif choice == '4':
      delete_recipe()
    
  
# Main Code ==================================================================================
# passing conn, cursor as arguments so they can be used in functions 

create_DB_table(conn, cursor)
main_menu(conn, cursor)
 