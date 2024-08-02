recipe_list = []
ingredients_list = []

def take_recipe():
  name = str(input("Input Name: "))
  cooking_time = int(input("Input cooking time: "))
  ingredients = list(input("Input list of ingredients (separated by comma): ").split(", "))
  recipe = {"Name": name, "Cooking-time": cooking_time, "Ingredients": ingredients}
  return recipe

n = int(input("How many recipes would you like to input? "))

for recipe in range(n):
  recipe = take_recipe()
  for ingredient in recipe["Ingredients"]: 
    if not ingredient in ingredients_list:
      ingredients_list.append(ingredient)
  recipe_list.append(recipe)

for recipe in recipe_list:
  if recipe["Cooking-time"] < 10 and len(recipe["Ingredients"]) < 4:
    recipe["Difficulty"] = "Easy"
  elif recipe["Cooking-time"] < 10 and len(recipe["Ingredients"]) >= 4:
    recipe["Difficulty"] = "Medium"
  elif recipe["Cooking-time"] >= 10 and len(recipe["Ingredients"]) < 4:
    recipe["Difficulty"] = "Intermediate"
  elif recipe["Cooking-time"] > 10 and len(recipe["Ingredients"]) >= 4:
    recipe["Difficulty"] = "Hard"
    
for recipe in recipe_list:
  print("Recipe: ", recipe["Name"])
  print("Cooking-time (min): ", str(recipe["Cooking-time"]))
  print("Ingredients: ")
  for ingredient in recipe["Ingredients"]:
    print(ingredient)
  print("Difficulty: ", recipe["Difficulty"])

def all_ingredients():
  print("Ingredients available across all recipes")
  print("_________________________________________")
  ingredients_list.sort()
  for ingredient in ingredients_list:
    print(ingredient)

all_ingredients()
