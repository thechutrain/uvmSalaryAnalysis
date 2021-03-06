from allYears_listData_dict import allYears_listData_dict  # this allows you to call & get all the data for 

import pandas as pd
pd.set_option('max_colwidth', 30) # This is so all the columns can show on my mac

def df_name_salary_position(year_str, sort_boolean):
    # create a local All_Data_Dict
    data = allYears_listData_dict()

    ### DECLARING LISTS ####
    #describes the hits of the unpaid leave employees
    index_hits = []
    salary_float = data[year_str]["salary_float"]
    salary_list = data[year_str]["salary_list"]
    position_list = data[year_str]["position_list"]
    employee_list = data[year_str]["employee_list"]

    ########### DEBUGGING ############

    if ((len(salary_float) == len(position_list)) and len(position_list) == len(employee_list)):
    	print "all incoming lists are the same length"
    else:
    	print len(salary_float)
    	print len(position_list)
    	print len(employee_list)
    ########## DEBUGGING ######
    # "06"
    # Debugging .... there is no Carr,Frances!!!!
  #   for i in range(len(employee_list)):
		# if ("Carr" in employee_list[i]):
		# 	print employee_list[i]
	# Fixed Yields:
			# Carr,Elizabeth Anne
			# Carr,Frances Eileen
			# Carr,Jacqueline B.
			# Carr,Jeanine M.
			# Devoid,Rick Carroll
			# Honeman,Carrie Ann
	# Previous yielded this below:
			# Carr,Elizabeth Anne
			# Carr,Jeanine M.
			# Carrard,Philippe
			# Carrigan,Linda Jean
			# Carris,Marschelle R.
			# Carroll Higgins,Linda Joan
			# Carroll,John A.
			# Clough,Carrie Mae
			# Honeman,Carrie Ann
			# Lewin,Carroll
			# MISSING PEOPLE:
			 # 'Carr,Frances Eileen',
			 # 'Carr,Jacqueline B.',

    ## DEBUGGING:
    # print len(salary_float)
    # print len(position_list)
    # print len(employee_list)
    # check_list = [1,100,500,1000,2000]
    # for i in range(len(check_list)):
    # 	index = check_list[i]
    # 	print ("******************")
    # 	print employee_list[index]
    # 	print salary_float[index]
    # 	print position_list[index]


#     #these will be the copies of the original lists, but without upl employees
    e_list = []
    p_list = []
    s_float = []
    s_list = []
    index_hits = []
    
    ## Take care of the UPL salary option ###
    for i in range(len(salary_float)):
        if (salary_float[i] != ""):
            pass
#             salary_float[i] = '{:20,.2f}'.format(salary_float[i])
        else:
            index_hits.append(i)
            salary_float[i] = 0
            
    for j in range(len(employee_list)):
        if (j in index_hits):
            pass
        else:
        	# Original code #########
            # e_list.append(employee_list[j])
            # p_list.append(position_list[j])
            # s_float.append(salary_float[j])
            ##########################
            try:
                e_list.append(employee_list[j])
	        p_list.append(position_list[j])
                s_list.append(salary_list[j])
	        s_float.append(salary_float[j])
            except:
            	print j





#     # Create a dataframe!!      
    # data = zip(e_list, p_list, s_float)
    data = zip(employee_list, position_list, salary_float)
    df = pd.DataFrame(data, columns=["Name", "Position", "Salary"])
    if (sort_boolean):
    	df = df.sort(["Salary"], ascending=False)

    return df
    
       
 #### CALL FUNCTION / TESTING #####
 ## if dataframe:
# a = df_name_salary_position("14", True)

# print (a.describe())
# print a

### No dataframe
# df_name_salary_position("06", True)
