# Exercise 1.5: Object-Oriented Programming in Python
## Learning Goals
- Apply object-oriented programming concepts to your Recipe app

## Reflection Questions

1. In your own words, what is object-oriented programming? What are the benefits of OOP?

  OOP is a programming paradigm that focuses on objects, python is composed of objects so this is a natural way of organizing your code when working with python. One of the main benefits is the conservation of declarations through inheritance, I can see how in building your own classes and sub classes it allows for cleaner code and an enjoyable way to organize your work.

2. What are objects and classes in Python? Come up with a real-world example to illustrate how objects and classes work.

  Classes are ways of classifying objects, or organizing them into structures that you determine. You can also apply your own methods to classes which lets you control the shifting of data more easily. Classes are like different pieces of choreography in dance. It is a way to organize the movement(data) into a defined phrases that can then be used or called in different ways.

3. In your own words, write brief explanations of the following OOP concepts;  

 - Inheritance
		Inheritance describes how classes can be “children” of “parent” classes. This allows the child class to inherit all of the methods and variables from the parent class. This is an endlessly stack-able process and can be developed to create complex inheritance structures, as I think about it thought I would not think that is advisable. This only works in one direction and parents can not inherit from their children. 

	- Polymorphism
		Polymorphism is when an attribute or method has the same name as one in another class. It allows the use of the same name and keeps the attribute or method distinct when they are called with their class. The example of the len() method is nice because it shows how it works differently with different kinds of data, when working with a string it will determine the number of characters but when working with a list it will determine the number of items on the list.

	- Operator Overloading
		Operator overloading is when you want to redefine or clarify how an operator works within an object. If you wanted to define a comparison operator like ‘<‘ then you would build a method within your class to determine how it functions. You define this by creating a method with the predetermined name of the operator and surrounding it with two underscore on each side, in this example of using the less than operator you would create ‘__lt__()’ 

