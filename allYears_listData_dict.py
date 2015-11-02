###################################################################
# This function makes a Dictionary of all the data!!! VERY IMPORTANT
# The key will be the year name as a string (96 ~ 14)


from makeRawList import makeRawList

def allYears_listData_dict():
	list_fileNames = ["sr96.txt", "sr97.txt", "sr98.txt", "sr99.txt", "sr00.txt", "sr01.txt", "sr02.txt", "sr03.txt", "sr04.txt", "sr05.txt", "sr06.txt", "sr07.txt", "sr08.txt", "sr09.txt", "sr10.txt", "sr11.txt","sr12.txt", "sr13.txt", "sr14.txt"]
	file_dir = "Data/"      # this is the directory the raw data is in
	All_Data_Dict = {}
	for i in range(len(list_fileNames)):
	    name = list_fileNames[i].replace("sr","")
	    name = name.replace(".txt", "")
	    # Call function here - makeRawList():
	    data_dict = makeRawList(file_dir + list_fileNames[i])

	    ### ADD CODE HERE
	    # Can add dataframes to each year:
	    # data_dict["df_avgSalary_position"] = 

	    All_Data_Dict[name] = data_dict

	return All_Data_Dict  # this dictionary has a string as key (Ex. "99"), and value is a dict containing the lists

# a = allYears_listData_dict()
