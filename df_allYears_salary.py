'''
The above code works,
now its time for me to make it into a cleaner function
'''

from allYears_listData_dict import allYears_listData_dict

import pandas as pd
import pprint
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'


### This will call a function that returns a dataframe for each year
def df_allYears_salary(master_dict):
    #code
    years = ["96", "97", "98", "99", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"] 
    for i in range(len(years)):
        y = years[i]  # gives you the year number as a string
        #salary for the year, including the unpaid leave values
        salary_upl = master_dict[y]["salary_float"]
        salary = []
        total_salary = 0
        employees = 0
        for k in range(len(salary_upl)):
            try:
                total_salary += salary_upl[k]
                salary.append(salary_upl[k])
                employees +=1
            except:
                # when you get an unpaid leave or upl
                pass
        if (i == 0):
            s = pd.DataFrame(salary, columns=[y])
        else:
            r = pd.DataFrame(salary, columns=[y])
            s = pd.concat([s, r], axis=1)
    return s # s is a dataframe object 


###### Call the function ######            
# master = allYears_listData_dict()
# df = df_allYears_salary(master)
# pprint.pprint(df)
    