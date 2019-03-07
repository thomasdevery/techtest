# Problem Description

In a programming language of your choice write some code to parse the exported data and
list the top 50 clients that have accumulated the most loyalty points since January 1st 2018.
Please exclude any banned clients.

# Programming Language of choice: Python

# ImportTest.py

I was able to import the csv files, assign the files to the DictReader.
Link the common attribute 'id' between the csv files.
Sort file content in decsening order based on the loyalty_points

# datamergetest.py

Testing page to merge seperate data values into an single string.

# Testing

I ran into difficulty when trying to print the data from multiple csv file onto one string
rather than seperate files. In <datamergetest.py> I was able to print the inputted data on
a single string but ran into difficulty when trying to do this with csv files.

I was able to sort the csv data into descending order based on the loyalty_points using
<sort = sorted(csv1, key=operator.itemgetter(3), reverse=True)> but not limit it to the top 50




