from df_avgSalary_position import df_avgSalary_position

######
# This function will call the df_avgSalary_position for each year
# and store this data in a dictionary, where the key will be a 
# string of the year name (ex. "99")

def allYears_df_avgSalary_position():
	master_dict = {}
	file_names = ["sr96.txt", "sr97.txt", "sr98.txt", "sr99.txt", "sr00.txt", "sr01.txt", "sr02.txt", "sr03.txt", "sr04.txt", "sr05.txt", "sr06.txt", "sr07.txt", "sr08.txt", "sr09.txt", "sr10.txt", "sr11.txt","sr12.txt", "sr13.txt", "sr14.txt"]
	for i in range(len(file_names)):
		id_num = file_names[i].replace("sr","")
		id_num = id_num.replace(".txt", "")
		# print id_num
		df = df_avgSalary_position(id_num, True)
		#enter the key-value pair into the master dict
		master_dict[id_num] = df

	# return the master dict
	return master_dict


# # CALL FUNCTION / TESTING 
# a = allYears_df_avgSalary_position()
# print a["00"]

