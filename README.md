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
- Exercise 1.4
  - practice tasks 1 - 2
  - recipe_input.py
  - recipe_search.py
  - recipe_data.bin
  - ipython-exercise1.4.png
  - updated-ipython-exercise1.4.png
  - journal
- Exercise 1.5
  - practice tasks 1- 3
  - recipe_oop.py
  - 1.5exercise-ipython 1 - 2
- Exercise 1.6
  - Practice tasks 1 - 2
  - ipython-1.6task 1 - 5
  - recipe_mysql.py
  - journal
- Exercise 1.7
  - Practice tasks 1 - 3
  - Task screen shots
  - recipe_app.py
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

## PyMySql instead of mysqlclient
trouble using mysqlclient as advized in the lesson. switched to pymysql. changes are as follows:

- adding mymysql in engine creation
   `engine = create_engine("mysql+pymysql://cf-python:password@localhost/my_database")`


