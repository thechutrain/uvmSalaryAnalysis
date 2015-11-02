from allYears_listData_dict import allYears_listData_dict  # this allows you to call & get all the data for 

import pandas as pd
pd.set_option('max_colwidth', 30) # This is so all the columns can show on my mac

def df_avgSalary_position(year_str, sort_boolean):
    # create a local All_Data_Dict
    data = allYears_listData_dict()

    ### temporary lists ####
    index_hits = []
    salary_float = data[year_str]["salary_float"]
    position_list = data[year_str]["position_list"]
    employee_list = data[year_str]["employee_list"] #for validation purpose!!!
    
    #set that contains a unique position
    unique_pos_set = set(position_list)  #makes
    ## Backbone of a potential dataframe
    unique_pos_list = []
    sum_salary = []
    index_employees = []
    avg_salary = []
    paid_employees_count = []
    
    # convert the set data to a a list
    while (len(unique_pos_set)!=0):     # checks to see if the unique_positions is not empty
        popped_off = unique_pos_set.pop()
        unique_pos_list.append(popped_off)        
        
    #### Loop through all the positions in the list
    ### see what indexes each employee matches to
    for i in range(len(unique_pos_list)):
        position_name = unique_pos_list[i]
        index_employees_matches = []
        for j in range(len(position_list)):
            if (position_list[j]==position_name):
                index_employees_matches.append(j)
            else:
                pass
        index_employees.append(index_employees_matches)
    
    
    # go through the list again, and add the sum salary for each list
    for i in range(len(unique_pos_list)):
        #initialize the total salary
        total_salary = 0
        unpaid_leave = 0
        for k in range(len(index_employees[i])):
            #index_employee[k]
            salary_index = index_employees[i][k]
            try:
                total_salary += salary_float[salary_index]
            except:
               unpaid_leave +=1
        sum_salary.append({"total": total_salary, "upl": unpaid_leave})

        
    # go through the list again, and add the sum salary for each list
    for i in range(len(unique_pos_list)):
        total_salary = sum_salary[i]["total"]
        # total paid employees is the number of employees minus unpaid
        total_employees = len(index_employees[i]) - sum_salary[i]["upl"]
        if (total_employees <= 0):
            average_salary = 0
        else:
            average_salary = total_salary / total_employees
#             avg_salary.append(average_salary)
        avg_salary.append('{:20,.2f}'.format(average_salary)) ### THIS IS FOR FORMATED Version, can't get sorted!
        # avg_salary.append(average_salary)
        paid_employees_count.append(total_employees)
#         avg_salary.append(format(average_salary, ".2"))
    
        
#     # Create a dataframe!!   
    data = zip(unique_pos_list, avg_salary, paid_employees_count)
    df = pd.DataFrame(data, columns=["Employee_Position", "Average_Salary", "Number_of_Employees"])
    if (sort_boolean):
    	df = df.sort(["Average_Salary"], ascending=False)
    print df
 #    if (sort_boolean):
	# 	df.sort(["Average Salary"], ascending=False)
	# return df
        
      
####### CALL FUNCTION / TESTING #####################   
b = df_avgSalary_position("06", True)
# print b