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
    position_list = data[year_str]["position_list"]
    employee_list = data[year_str]["employee_list"] 
    ## DEBUGGING:
    print len(salary_float)
    print len(position_list)
    print len(employee_list)
    check_list = [1,100,500,1000,2000]
    for i in range(len(check_list)):
    	index = check_list[i]
    	print ("******************")
    	print employee_list[index]
    	print salary_float[index]
    	print position_list[index]

    #these will be the copies of the original lists, but without upl employees
#     e_list = []
#     p_list = []
#     s_float = []
    
#     ## Take care of the UPL salary option ###
#     for i in range(len(salary_float)):
#         if (salary_float[i] != ""):
#             pass
# #             salary_float[i] = '{:20,.2f}'.format(salary_float[i])
#         else:
#             index_hits.append(i)
#             salary_float[i] = 0
            
#     for j in range(len(employee_list)):
#         if (j in index_hits):
#             pass
#         else:
#             e_list.append(employee_list[j])
#             p_list.append(position_list[j])
#             s_float.append(salary_float[j])
# #     # Create a dataframe!!      
#     # data = zip(e_list, p_list, s_float)
#     data = zip(employee_list, position_list, salary_float)
#     df = pd.DataFrame(data, columns=["Name", "Position", "Salary"])
#     if (sort_boolean):
#     	df = df.sort(["Salary"], ascending=False)
#     return df
    
        


 #### CALL FUNCTION / TESTING #####
 ## if dataframe:
# a = df_name_salary_position("00", True)
# print (a.describe())
# print a

### No dataframe
df_name_salary_position("00", True)