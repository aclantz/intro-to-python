import pickle 

def display_recipe(recipe):
  print("_____ Recipe _____")
  print("Name: " + recipe["name"])
  print("Cooking-time: " + str(recipe["cooking_time"]) + "min")
  print("Ingredients: ")
  for item in recipe["ingredients"]:
    print(item)
  print("Difficulty: " + recipe["difficulty"])

def search_ingredients(data):
  print("All ingredients: ")
  for item, value in enumerate(data["all_ingredients"]): #is this formatted correctly?
    print(str(item) + " " + str(value))
  try:
    n = input("Pick an ingredient number to search: ")
    ingredient_searched = data["all_ingredients"[n]]
  except:
    "Input value does not have a match"
  else:
    for recipe in data["recipe_list"]:
      if ingredient_searched in recipe["ingredients"]:
        display_recipe(recipe) #why is this not displaying? 

#Main code ---------------
data_file = input("Input tha name of your recipe data file? ") #recipe_data.bin
try:
  with open(data_file, 'rb') as my_file:
    data = pickle.load(my_file)
except:
  "No file found w/ that name"
else:
  search_ingredients(data)

