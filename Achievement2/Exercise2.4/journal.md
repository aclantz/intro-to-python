# Exercise 2.4: Django Views and Templates

## Learning Goals
- Summarize the process of creating views, templates, and URLs 
- Explain how the “V” and “T” parts of MVT architecture work
- Create a frontend page for your web application

## Reflection Questions
1. Do some research on Django views. In your own words, use an example to explain how Django views work.
    Views are the means in which Django organizes the “pages” of your webpage, or aspects of your webpage. The combination of views and templates is the strict format that Django uses to know which views are being used at which times and creates the URLs that are then used by the browser/user.

2. Imagine you’re working on a Django web development project, and you anticipate that you’ll have to reuse lots of code in various parts of the project. In this scenario, will you use Django function-based views or class-based views, and why?
    If I was needing to use a lot of the same code I would use CBV. The class system allows for cleaner simpler code that can then be used over and over again. If I needed to build something that had a lot of special specifics and exceptions I would use FBV as with functions you can build exact specific functions to be called.


3. Read Django’s documentation on the Django template language and make some notes on its basics.
    Django’s DTL is its own template system that is synced with its built-in backend logic. Its a way to write presentation focused code like HTML but with some extra programming features. For example using a variable in the code ( signified by: {{ variable }} ), or calling a for loop, or using filters to adjust variables. This seems very convenient when working with language as simple as HTML, it gives you more means of connecting all of the data within your project while displaying it. 
