'''
The above code works,
now its time for me to make it into a cleaner function
'''

from allYears_listData_dict import allYears_listData_dict
from df_allYears_salary import df_allYears_salary # imports the function that returns the dataframe of all salaries of all years

import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.mpl_style = 'default'


def boxplot_salary_allYears():      
    # make the master dictionary of all the data  
    master = allYears_listData_dict()
    # make a dataframe of all the salaries for a year, for all the data
    df = df_allYears_salary(master)
    plt.figure()
    df.boxplot(return_type='axes')
    ## add title and label axis
    plt.ylabel('Salary (USD)')
    plt.xlabel("School Year")
    plt.title("Distribution of UVM employee salary from 1996 - 2014")
    plt.show(block=True)  # this is code is needed if run outside of canopy

###### call function / testing
boxplot_salary_allYears()
