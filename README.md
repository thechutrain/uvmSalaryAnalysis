Author: Alan Chu
Date: November 1, 2015

Purpose: The purpose of this project was to see if there were any relations within salary trends among administrative employees versus various teaching positions, over a 15 year trend at UVM.

Project Outline:
1.) Downloaded all Employee Data from UVM website as pdf files. Example file name is sr##.pdf

2.) Used terminal pdftotext to convert all pdf files to a raw txt file. *Note: did not use the raw command (ex. pdftotext sr##.pdf -r) which returned each employee on the same line, as I had trouble with the regular expression, separating employee name and position in some weird scenarios!

3.)Use rawFile_to_pandaDF.py to do a basic cleaning process of the raw text file, and store the data as a dataframe for analysis.

4.) 
