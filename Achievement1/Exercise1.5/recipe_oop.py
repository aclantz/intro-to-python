class Recipe(object):

  all_ingredients = set()

  def __init__(self, name, ingredients, cooking_time):
    self.name = name
    self.ingredients = ingredients
    self.cooking_time = cooking_time
    self.difficulty = None

  # getter methods --------------------
  def get_name(self):
    # get name of recipe
    output =  "Recipe name: " + self.name
    return output
  def get_cooking_time(self):
    # get cooking time of recipe
    output = "Cooking time: " + str(self.cooking_time)
    return output
  
  # ***** this is not working *****
  def get_ingredients(self): 
    # get ingredients of recipe
    print("Ingredients: \n")
    for item in self.ingredients:
      print(item + ', ')

  def get_difficulty(self):
    # get difficulty of recipe, set difficulty if not assigned
    if self.difficulty == None:
      self.difficulty = self.calculate_difficulty()
      output = "recipe difficulty: " + self.difficulty
      return output
    else:
      output = "recipe difficulty: " + self.difficulty
      return output
  
  # setter methods --------------------
  def set_name(self):
    self.name = input("Input recipe name: ")
  def set_cooking_time(self):
    self.cooking_time = int(input("Input recipe cooking time (min): "))

  # methods --------------------
  def add_ingredients(self, *items): 
    # add ingredients to list in recipe
    for item in items:
      self.ingredients.append(item)
      self.update_all_ingredients(item)

  def calculate_difficulty(self):
    # set difficulty of recipe based on cooking time and length of ingredient list
    if self.cooking_time < 10 and len(self.ingredients) < 4:
      self.difficulty = "Easy"
    elif self.cooking_time < 10 and len(self.ingredients) >= 4:
      self.difficulty = "Medium"
    elif self.cooking_time >= 10 and len(self.ingredients) < 4:
      self.difficulty = "Intermediate"
    elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
      self.difficulty = "Hard"
    return self.difficulty

  def search_ingredient(self, item):
    # search if ingredient is in recipe ingredients list, return boolean
    return item in self.ingredients

  def update_all_ingredients(self):
    # add ingredient to global variable all_ingredients if not already in list
    for item in self.ingredients:
      if item not in Recipe.all_ingredients:
        Recipe.all_ingredients.append(item)

  # list of ingredients is not working *****
  def __str__(self):
      # define how to print recipe
      self.calculate_difficulty()  # Ensure difficulty is calculated
      ingredients_str = "\n".join(self.ingredients)  
      output = "--- Recipe ---" + \
              "\nName: " + self.name + \
              "\nCooking-Time (min): " + str(self.cooking_time) + \
              "\nDifficulty: " + str(self.difficulty) + \
              "\nIngredients:\n" + ingredients_str # ***** This is not working *****
      return output
  
  def recipe_search(data, input):
    # search for ingredient in a recipe and return the recipe if present
    for recipe in data:
        if Recipe.search_ingredient(recipe, input):
          print(recipe)
    
    

# Main code ------------------------------

tea_recipe = Recipe("Tea", ["tea-Leaves", "sugar", "water"], 5)
coffee_recipe = Recipe("Coffee", ["coffee-ground", "sugar", "water"], 5)
cake_recipe = Recipe("Cake", ["sugar", "butter", "eggs", "vanilla extract", "flour", "baking powder", "milk"], 50)
banana_smoothie_recipe = Recipe("Banana Smoothie", ["bananas", "milk", "peanut butter", "sugar", "ice-cubes"], 5)

print(tea_recipe)
print(coffee_recipe)
print(cake_recipe)
print(banana_smoothie_recipe)

recipes_list = [tea_recipe, coffee_recipe, cake_recipe, banana_smoothie_recipe]
ingredient_list = ["water", "sugar", "bananas"]

for ingredient in ingredient_list:
  print("--- Searched recipes for " + ingredient + "--- Matches include:\n" )
  Recipe.recipe_search(recipes_list, ingredient)
