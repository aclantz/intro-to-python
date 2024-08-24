# Exercise 2.2: Django Project Set Up

## Learning Goals
- Describe the basic structure of a Django project 
- Summarize the difference between projects and apps
- Create a Django project and run it locally
- Create a superuser for a Django web application

## Reflection Questions
1. Suppose you’re in an interview. The interviewer gives you their company’s website as an example, asking you to convert the website and its different parts into Django terms. How would you proceed? For this question, you can think about your dream company and look at their website for reference. 
(Hint: In the Exercise, you saw the example of the CareerFoundry website in the Project and Apps section.)
    If I use DataRobot as an example, I would create the dataRobot project, its apps would include Login, contact, userInfo, operate, govern, and build. This focuses on the key tasks or abilities of the website and narrows them down into apps. 

2. In your own words, describe the steps you would take to deploy a basic Django application locally on your system. 
    		Once the project was already created I would make sure that the database is created by running `python manage.py migrate` and from there would run `python manage.py runserver` connecting to the server link to see that its running.

3. Do some research about the Django admin site and write down how you’d use it during your web application development.
    I could use the admin interface to manage users, the example used in the documentation talks about using it to manage articles being either published, in process, or withdrawn. I feel like using it to manage site content assuming everything is built and created but you wanted to be able to shift the content externally. Managing users would be useful even to just see a list of users or to find one if there is a reported problem. 
