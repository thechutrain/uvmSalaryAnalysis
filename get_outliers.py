##### IMPORT STATEMENTS: #####
from allYears_listData_dict import allYears_listData_dict
from df_allYears_salary import df_allYears_salary
import pandas as pd
import pprint
pd.set_option('max_colwidth', 30) # This is so all the columns can show on my mac


# TEMPORARY ##################################
# make a local reference of the master dictionary of all the data
master = allYears_listData_dict()


def get_outliers(year_str, master_dict):
#     # make a local reference of the master dictionary of all the data
#     master = allYears_listData_dict()
#     #make the complete dataframe of all years
    df_allSalary= df_allYears_salary(master_dict)
    
    # Find out what the upper bound for top outliers is:
    std = df_allSalary.loc[:, year_str].std()
    mean = df_allSalary.loc[:, year_str].mean()
    upper_bound = mean + (2*std)
    # making a copy
    # df_copy = df_allSalary.loc[:,year_str].copy()
    # df_copy = [df_copy > upper_bound]
    # print df_copy
    
    # Initialize variables for outliers
    index_outliers = [] # collects the index of outlier
    salary_outliers = []  #gets the float salary of outliers
    positions_outliers = []
    name_outliers = []
    
    # get the list of salary data, & see if salary is greater than upper_bound
    # This gets the outliers & upl employees
    year_salary = master_dict[year_str]['salary_float']
    for i in range(len(year_salary)):
        if ((year_salary[i] > upper_bound) and (year_salary[i]!= "" or 0)) :
            salary_outliers.append(year_salary[i])
            index_outliers.append(i)
        else:
            pass
    
    # get the names of the outliers
    year_names = master_dict[year_str]['employee_list']
    for i in range(len(index_outliers)):
        index = index_outliers[i]
        name_outliers.append(year_names[index])
#     pprint.pprint(name_outliers)
        
    # get the positions of the outliers
    year_positions = master_dict[year_str]['position_list']
    for i in range(len(index_outliers)):
        index = index_outliers[i]
        positions_outliers.append(year_positions[index])
#     pprint.pprint(positions_outliers)
######## DEBUGGING #################
    # print len(positions_outliers)
    # print len(index_outliers)
    # print len(salary_outliers)
    # print len(name_outliers)
    # print positions_outliers[-1]
    # print index_outliers[-1]
    # print salary_outliers[-1]
    # print name_outliers[-1]

    # create a dataframe
    data = zip(name_outliers, positions_outliers, salary_outliers)
    pprint.pprint(data)
    df = pd.DataFrame(data, columns=["Name", "Position", "Salary"])
    df = df.sort(['Salary'], ascending=False)
    return df
    
#CALL THE FUNCTION/ Testing
a = get_outliers("14", master)
# a.to_csv(path_or_buf="outliers_data_14.csv") # makes a csv file of the data!!
    
