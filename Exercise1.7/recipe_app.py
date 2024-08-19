# imports
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base  # changed from sqlalchemy.exe.declarative
from sqlalchemy import Column
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import sessionmaker
import time

# connect to DB
engine = create_engine("mysql+pymysql://cf-python:password@localhost/my_database")
Base = declarative_base()
# session object to manage DB connection
Session = sessionmaker(bind=engine)
session = Session()


class Recipe(Base):
    # base model for recipe class
    # name of table
    __tablename__ = "final_recipes"
    # table attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # methods ------------------------------
    def __repr__(self):
        # display for simple call of recipe
        return (
            "<Recipe ID: "
            + str(self.id)
            + " - Name: "
            + self.name
            + " - Difficulty: "
            + self.difficulty
            + +">"
        )

    def __str__(self):
        # display for print() or recipe
        ingredients_list = self.ingredients.split(", ")
        ingredients_str = "\n".join([f"\t{item}" for item in ingredients_list])

        return (
            f"{self.name} Recipe\n"
            f"{'_'*20}\n"
            f"Recipe ID: {self.id}\n"
            f"Recipe Name: {self.name}\n"
            f"Cooking-time: {self.cooking_time} min\n"
            f"Difficulty: {self.difficulty}\n"
            "Ingredients:\n"
            f"{ingredients_str}\n"
        )

    def calculate_difficulty(self, cooking_time, ingredients):
        # calculate the difficulty based on two provided arguments
        if cooking_time < 10 and len(ingredients) < 4:
            difficulty = "Easy"
        elif cooking_time < 10 and len(ingredients) >= 4:
            difficulty = "Medium"
        elif cooking_time >= 10 and len(ingredients) < 4:
            difficulty = "Intermediate"
        elif cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = "Hard"
        return difficulty  # unsure of this *****************************

    def return_ingredients_as_list(self):
        # take ingredient string and change into list
        ingredients = self.ingredients
        if ingredients != " ":
            ingredients.split(", ")
        else:
            return []


# create table on DB
Base.metadata.create_all(engine)


# functions for main menu
# ------------------------------------------------------------------------------------------------------
def create_recipe():
    # Create a recipe to be stored in your recipes database
    print("Create a new Recipe to submit! ")
    print("-" * 30)
    # intake data for new recipe
    while True:
        name = input("Recipe name (50 characters or less): ")
        if len(name) <= 50:
            break
        else:
            print("\tTry choosing a simpler name, it's just a recipe calm down.")
    while True:
        cooking_time = input("Cooking-time (numerical input please): ")
        if cooking_time.isnumeric():
            cooking_time = int(cooking_time)
            break
        else:
            print("\tNumbers only please. Try again...")
    while True:
        ingrd_number = input("Number of ingredients in recipe: ")
        if ingrd_number.isnumeric():
            ingrd_number = int(ingrd_number)
            break
        else:
            print("\tNumbers only please. Try harder this time")

    # get ingredients
    ingredients = []
    print("Great! Input your ingredients one by one")
    for _ in range(ingrd_number):
        item = input("Add an ingredient: ")
        ingredients.append(item)
    ingredients_str = (", ").join(ingredients)

    # new recipe object
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients_str,
        difficulty=Recipe.calculate_difficulty(Recipe, cooking_time, ingredients),
    )
    # upload new entry to DB
    session.add(recipe_entry)
    session.commit()
    print("Recipe added!")


# ------------------------------------------------------------------------------------------------------
def view_all_recipes():
    # view all recipe data in DB
    # retrieve all recipes as list
    recipe_list = session.query(Recipe).all()

    if recipe_list == []:
        print("No recipes added to database yet")
        return None
    else:
        for recipe in recipe_list:
            print(recipe)


# ------------------------------------------------------------------------------------------------------
def search_by_ingredients():
    # search for recipes by ingredient
    # check is DB table has any entries
    table_count = session.query(Recipe).count()
    if table_count < 1:
        print("No recipes added to database yet")
        return None

    # retrieve all ingredients in table
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    # format ingredients into one list
    for result in results:
        ingrd_list = result[0].split(", ")
        all_ingredients.extend(ingrd_list)
    # remove duplicate ingredients
    sorted_ingredients = sorted(set(all_ingredients))

    # display all ingredients with index number
    print("All of the Ingredients:")
    print("_" * 20)
    for index, ingredient in enumerate(sorted_ingredients):
        print(f"\t{index} {ingredient}")
    # user input for ingredient
    print()
    ingrd_choice = input(
        "Choose ingredient, by number, to search for (please separate with spaces): "
    )
    print()

    # results of user input
    try:
        # convert choices to int and map to selected ingredients
        selected_ingredients = [
            sorted_ingredients[int(choice)] for choice in ingrd_choice
        ]
    except (ValueError, IndexError):
        print("\tYou chose an invalid option. Try again.")
        return None
    # build query
    conditions = []
    for ingredient in selected_ingredients:
        like_term = Recipe.ingredients.like(f"%{ingredient}%")
        conditions.append(like_term)
    # query DB and display results
    results = session.query(Recipe).filter(*conditions).all()
    if results:
        for recipe in results:
            print(recipe)
    else:
        print("\tNo recipes found with that ingredient")


# ------------------------------------------------------------------------------------------------------
def edit_recipe():
    # edit recipes
    # check is DB table has any entries
    table_count = session.query(Recipe).count()
    if table_count < 1:
        print("No recipes added to database yet")
        return None
    # display recipes
    results = session.query(Recipe.id, Recipe.name).all()
    print("Recipes")
    print("_" * 20)
    print()
    for result in results:
        print(f"ID: {result.id}")
        print(f"Name: {result.name}")
        print()

    # choose recipe to edit
    recipe_choice = int(input("Choose a recipe to edit and input the ID: "))
    if recipe_choice not in [result.id for result in results]:
        print("I am so sorry you choose an option that doesn't exist. Like really??")
        return None

    # display chosen recipe
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_choice).first()
    print()
    print(f"Recipe ID: {recipe_to_edit.id}")
    print("_" * 20)
    print(f"1. Name:  {recipe_to_edit.name}")
    print(f"2. Cooking-time: {recipe_to_edit.cooking_time}min")
    print("3. Ingredients: ")
    ingredients = recipe_to_edit.ingredients.split(", ")
    for ingrd in ingredients:
        print(f"\t{ingrd}")
    print()
    # choose attribute to edit
    edit_choice = int(input("Choose an attribute, by number, to edit: "))

    # edit options
    if edit_choice == 1:
        # edit name
        while True:
            name_edit = input("Input the new recipe Name (50 characters or less): ")
            if len(name_edit) <= 50:
                recipe_to_edit.name = name_edit
                break
            else:
                print(
                    "This is a terrible name choice. Try again with less than 50 characters."
                )
    elif edit_choice == 2:
        # edit cooking time
        while True:
            cooking_time_edit = input("Input a new Cooking-time (min): ")
            if cooking_time_edit.isnumeric():
                cooking_time_edit = int(cooking_time_edit)
                recipe_to_edit.cooking_time = cooking_time_edit
                break
            else:
                print("next time please keep to numbers and not letters")
    elif edit_choice == 3:
        # choose how to edit ingredients
        print("Would you like to: ")
        print("1. Add ingredients to the list")
        print("2. Remove ingredients from the list")
        ingrd_edit_choice = int(
            input("Choose the number of the option you would like to do: ")
        )

        if ingrd_edit_choice == 1:
            # add ingredients
            while True:
                ingrd_add = input(
                    "Input ingredients you would like to add (separate with comma): "
                )
                if ingrd_add:
                    new_ingredients = ingrd_add.split(", ")
                    updated_ingredients = ingredients + new_ingredients
                    recipe_to_edit.ingredients = (", ").join(updated_ingredients)
                    break
                else:
                    print("Something didn't work, try again.")
        elif ingrd_edit_choice == 2:
            # remove ingredients
            while True:
                ingrd_remove = input(
                    "Input ingredients you would like to remove (separate with comma): "
                )
                if ingrd_remove:
                    remove_ingredients = ingrd_remove.split(", ")
                    updated_ingredients = [
                        ingrd
                        for ingrd in ingredients
                        if ingrd not in remove_ingredients
                    ]
                    recipe_to_edit.ingredients = (", ").join(updated_ingredients)
                    break
                else:
                    print("Something didn't work, try again")

    # calc difficulty
    ingrd_list = recipe_to_edit.ingredients.split(", ")
    new_difficulty = Recipe.calculate_difficulty(
        Recipe, recipe_to_edit.cooking_time, ingrd_list
    )
    recipe_to_edit.difficulty = new_difficulty
    # commit changes to DB
    session.commit()
    print("Edits complete!")


# ------------------------------------------------------------------------------------------------------
def delete_recipe():
    # delete a recipe from the DB table
    # check is DB table has any entries
    table_count = session.query(Recipe).count()
    if table_count < 1:
        print("No recipes added to database yet")
        return None
    # display recipes
    results = session.query(Recipe.id, Recipe.name).all()
    print("Recipes")
    print("_" * 20)
    print()
    for result in results:
        print(f"ID: {result.id}")
        print(f"Name: {result.name}")
        print()

    # choose recipe to be deleted
    recipe_choice = int(input("Choose a recipe to delete and input the ID: "))
    # check if id is in results
    valid_ids = [result.id for result in results]
    if recipe_choice not in valid_ids:
        print("I am so sorry you choose an option that doesn't exist. Like really??")
        return None

    # confirm choice
    print(f"Are you sure you want to delete Recipe ID: {recipe_choice}")
    confirm = input(
        "Yes or No, input y/n: "
    )  # add .strip.lower() handles case variation and extra spaces ???
    if confirm == "y":
        # retrieve recipe from DB, delete, commit
        recipe_to_delete = (
            session.query(Recipe).filter(Recipe.id == recipe_choice).first()
        )
        if recipe_to_delete:
            session.delete(recipe_to_delete)
            session.commit()
            print(f"Recipe ID: {recipe_choice} was deleted.")
        else:
            print("Recipe not found")
    else:
        print("No recipe was deleted")
        return None


# ------------------------------------------------------------------------------------------------------
def main_menu():
    # display loop
    while True:
        # print()
        # print("____________RECIPE APP____________")
        print()
        print("\tMain Menu")
        print("\t---------")
        print("\t1. Create a new recipe")
        print("\t2. View all recipes")
        print("\t3. Search for recipes by ingredient")
        print("\t4. Edit recipe")
        print("\t5. Delete recipe")
        print("\t6. Exit")
        print()

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            print()
            create_recipe()
        elif choice == "2":
            print()
            view_all_recipes()
        elif choice == "3":
            print()
            search_by_ingredients()
        elif choice == "4":
            print()
            edit_recipe()
        elif choice == "5":
            print()
            delete_recipe()
        elif choice == "6":
            print("Bye!")
            session.commit()
            session.close()
            # engine.close()
            break
        else:
            print("Invalid choice, try again")

        # delay before printing main menu loop post function 
        time.sleep(2)


# Main Code =================================================================================================
print()
print("____________RECIPE APP____________")
main_menu()
