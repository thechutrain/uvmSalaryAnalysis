Author: Alan Chu
Date: November 1, 2015

Purpose: The purpose of this project was to see if there were any relations within salary trends among administrative employees versus various teaching positions, over a 15 year trend at UVM.

Project Outline:
1.) Downloaded all Employee Data from UVM website as pdf files. Example file name is sr##.pdf

2.) Used terminal pdftotext to convert all pdf files to a raw txt file. *Note: did not use the raw command (ex. pdftotext sr##.pdf -r) which returned each employee on the same line, as I had trouble with the regular expression, separating employee name and position in some weird scenarios!

<strike>
3.)Use rawFile_to_pandaDF.py to do a basic cleaning process of the raw text file, and store the data as a dataframe for analysis.
</strike>

#Part I: Data Cleaning & Processing
includes step 1 & 2
3.) <b> allYears_listData_dict() </b> : important function that returns the master dictionary that stores all the data. The keys are strings of the last two numbers of the year (ex. "01") and the value is a dictionary of lists (ex. {"salary_list": salary_list, "emloyee_list": employee_list, "position_list": position_list, "salary_float": salary_float}) 

<b> allYears_listData_dict() </b> within its for loop, calls the function <b> makeRawList("rawfile") </b> which returns a dictionary of the lists of data
 
