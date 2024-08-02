# intro-to-python
Career Foundry, Specialization Python, Achievement 1

## Content
- Exercise 1.1
  - add.py
  - hello.py
  - requirements.txt
  - Journal 
- Exercise 1.2
  - practice tasks 1 - 5
  - task img 1
  - task img 2
  - Journal
- Exercise 1.3
  - practice tasks 1 - 3
  - add.py
  - name.capitolizer.py
  - exercise_1.3.py
  - 1.3exercise-ipython.png
  - journal

## Objective 
Build the command line version of a Recipe app, which acts as a precursor to its
web app counterpart in Achievement 2.

### Key features
- Create and manage the user’s recipes on a locally hosted MySQL database.
- Option to search for recipes that contain a set of ingredients specified by the user.
- Automatically rate each recipe by their difficulty level.
- Display more details on each recipe if the user prompts it, such as the ingredients, cooking time,
and difficulty of the recipe.

## Exercise 1.2
I have chosen to have my recipe structure to be a dictionary. I think because each recipe is going to be full different sections that suit key-value pairs (e.g. Cooking-time: 5 min, Ingredients: [ …] ) this feels like the natural format. Each key will also hold a mix of value types and this suits dictionaries.

For my outer structure I am going to use a List to store my recipe dictionaries. If we are looking for structure that is sequential, and allows for easy adjustment, I think a List suits this best because it is mutable and allows for modifications, additions, and deletions.
