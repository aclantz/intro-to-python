# Exercise 1.4: File Handling in Python
## Learning Goals
- Use files to store and retrieve data in Python

## Reflection Questions
1. Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

    If you didn’t store local files it would become hard/inconvenient to work with any data as it would be lost 
    after you finish running any scripts.


2. In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles?
In which situations would you choose to use pickles and why? 

    Pickles are binary files that store complicated data in a way that we can not read. This is useful when 
    you want to store something that is more complex like a dictionary with different data types.

3. In Python, what function do you use to find out which directory you’re currently in? What if you wanted 
to change your current working directory?

    os.getcwd() - find your currant working directory
		os.chdir() - change your directory

4. Imagine you’re working on a Python script and are worried there may be an error in a block of code. 
How would you approach the situation to prevent the entire script from terminating due to an error?

    Using Try blocks allows you to “try” executing different parts of your code and giving guidelines for what to do if there is an error so that the script doesn’t terminate. 


5. You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. 
How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need 
more practice with? Feel free to use these notes to guide your next mentor call. 

    I am feeling proud of how I went through this last task. I used to be scared to start writing code and I felt better just writing and trying something even if it was wrong, and then correcting from there. I still feel inexperienced and when I look at some of the example code from other students I get overwhelmed with the complexity they are using. I worry that my code is very simple.
