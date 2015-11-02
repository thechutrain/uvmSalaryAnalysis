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
includes step 1.) and 2.)
3.) allYears_listData_dict() --> no arguments needed, returns a dictionary of all the Data from the "sr##.pdf" files
	* it calls the function: makeRawList("rawfile") --> returns a dictionary containing the list data on employee, position, salary for a specific year
	* makeRawList --> calls makeCleanFile("filename") --> which makes a "clean_sr##.txt" and returns the name of the cleanfile
