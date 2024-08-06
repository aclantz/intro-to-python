import pickle


def take_recipe():
    name = input("Recipe name: ")
    cooking_time = int(input("Cooking time (min): "))
    ingredients = list(input("Ingredients (separate with comma): ").split(", "))
    difficulty = calc_difficulty(cooking_time, ingredients)

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }
    return recipe


def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"

    return difficulty


# Main code ------------
bin_file = print(input("Choose a .bin file: "))
try:
    data = pickle.load(bin_file, "rb")
except FileNotFoundError:
    "File not found"
    data = {"recipes_list": [], "all_ingredients": []}
except:
    "Oops unknown error"
    data = {"recipes_list": [], "all_ingredients": []}
else:
    bin_file.close()
finally:
    recipe_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


n = int(input("How many recipes would you like to enter? "))
for recipe in range(n):
    recipe = take_recipe()
    recipe_list.append(recipe)
    for items in recipe["ingredients"]:
        if not items in all_ingredients:
            all_ingredients.append(items)

data = {"recipe_list": recipe_list, "all_ingredients": all_ingredients}
with open("recipe_data.bin", "wb") as my_file:
    pickle.dump(data, my_file)
