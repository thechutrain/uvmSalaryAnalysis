from allYears_listData_dict import allYears_listData_dict    # make a master dictionary of all the data
from df_name_salary_position import df_name_salary_position  # creates the dataframe for each year of name, pos, salary_float

# import pandas as pd      # will be imported from df_name_salary_position
import pprint

def make_csv_allData():
	# code for making the data
	# create the master dictionary - key is "96" of the year, and value is the dictionary
	master_dictionary = allYears_listData_dict()
	k_years = ["96", "97", "98", "99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"] 

	# test to see whats in master_dicitonary
	# pprint.pprint(master_dictionary[k_years[0]]) # returns a dictionary of lists *salary contains upl

	

#### test & call the function
make_csv_allData()