from allYears_listData_dict import allYears_listData_dict    # make a master dictionary of all the data
from df_name_salary_position import df_name_salary_position  # creates the dataframe for each year of name, pos, salary_float

import pandas as pd      # will be imported from df_name_salary_position
import pprint

def make_csv_allData():
	# code for making the data
	# create the master dictionary - key is "96" of the year, and value is the dictionary
	master_dictionary = allYears_listData_dict()
	k_years = ["96", "97", "98", "99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"] 

	# test to see whats in master_dicitonary
	# pprint.pprint(master_dictionary[k_years[0]]) # returns a dictionary of lists *salary contains upl
	df_list = []
	for y in range(len(k_years)):
		year_data = master_dictionary[k_years[y]]
		df = df_name_salary_position(k_years[y], True)
		# check to see if all the lists are the same lengths:
		year_list = []
		if (len(year_data["salary_list"]) == len(year_data["employee_list"]) and len(year_data["position_list"])):
			year_str = k_years[y]
			if (int(year_str)<20):     # will have to change after 2020!
				year_str = "20" + year_str
			else:
				year_str = "19" + year_str
			# print year_str
			year_list = [year_str] * len(year_data["salary_list"])
		# pprint.pprint(year_list)
		# add the new column of the data to dataframe of name, position, salary
		df["Year"] = year_list
		df_list.append(df)
	# made a list of the data frame! time to concatonate it
	df_allData = pd.concat(df_list)
	# pprint.pprint(df_allData)

	# Make a csv of all the data!
	df_allData.to_csv(path_or_buf="uvm_employee_salary_data_1994-2014.csv", index=False, columns = ["Year", "Name", "Position", "Salary"])


			# print len(year_data["salary_list"])
			# print k_years[y]
		# pprint.pprint(df_list)

	# testing, to make at dataframe with a column that has the year 1994
	# df_94 = pd.DataFrame()
	# pprint.pprint(all_data.head(10))

#### test & call the function
make_csv_allData()