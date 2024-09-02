# Exercise 2.6: User Authentication in Django

## Learning Goals
- Create authentication for your web application
- Use GET and POST methods 
- Password protect your web application’s views

## Reflection Questions
1. In your own words, write down the importance of incorporating authentication into an application. You can take an example application to explain your answer. 
    Authentication is what “protects” your content on an application. If you had created an app that curated content depending on what the user chose as its focus then you wouldn’t want anyone to be able to access that curated collection. Authenticating the user allows them to be able to see something that is just theirs. 

2. In your own words, explain the steps you should take to create a login for your Django web application. 
    - Create a new `view.py` in your main project folder
		- create the view within it
		- Create a template folder in your src folder, another auth folder within that, and a new login.html within that
		- fill in your template
		- register your view in the project urls.py file
		- make sure your settings.py knows where the new templates folder is and the login file within.


3. Look up the following three Django functions on Django’s official documentation and/or other trusted sources and write a brief description of each.
    authenticate()  - Used to verify a users credentials
    redirect()      - Used to bring a user to another URL
    include()       - Used to add other URL configurations to the main URL config. Organizes URL patterns



