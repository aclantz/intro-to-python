# Exercise 2.7: Data Analysis and Visualization in Django

## Learning Goals
- Work on elements of two-way communication like creating forms and buttons
- Implement search and visualization (reports/charts) features
- Use QuerySet API, DataFrames (with pandas), and plotting libraries (with matplotlib)

# Reflection Questions
1. Consider your favorite website/application (you can also take CareerFoundry). Think about the various data that your favorite website/application collects. Write down how analyzing the collected data could help the website/application. 
    Data analysis can help a website like YouTube to understand what kind of videos are being uploaded and to then help provide users with more accurate suggestions. 

2. Read the Django official documentation on QuerySet API. Note down the different ways in which you can evaluate a QuerySet.
    - iteration
		- pickling/caching
		- repr()
		- len()
		- list()
		- bool()
		- you can use exists() but only to return a boolean answer if it exists or not

3. In the Exercise, you converted your QuerySet to DataFrame. Now do some research on the advantages and disadvantages of QuerySet and DataFrame, and explain the ways in which DataFrame is better for data processing.
    DataFrames are useful when handling large amounts of data and also give you more data analysis tools to manipulate the data. Tools to help with data manipulation include tools like pivoting, reshaping, and statistical analysis. 
