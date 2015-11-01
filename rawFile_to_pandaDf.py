###################################################################
# This function will take in the raw text file of the data where employee
# name, posiiton and salary are all jumbled up and will organize it
# into lists that will then be put into a data frame


################## IMPORT Statements ###############################
import pprint
import pandas as pd

################### sep_rawFile_to_panda_df() ############################
def rawFile_to_pandaDf(raw_file):
    # see if filename is a string
    if (type(raw_file) != str):
        print("Error! Filename must be a string")
        # exit here? 
    else:
        pass

    # # create a new filename that is clean_filename 
    lines = [line.rstrip('\n') for line in open(raw_file)]
    
    ### Organize the lines into temporary lists and append them to the 3 separate lists
    first_empty = True   # boolean that toggles to see if its firsttime its empty
    temp_list = []       # temporary list that holds data
    employee_list = []   # employee names
    position_list = []   # holds the position of employees
    salary_list = []     # holds all the salaries
    choice = 1

    for line in lines:
        if (line == ''):  #checks to see if line is empty
            #check to see if first empty
            if (first_empty):     # if it is the first empty, pass & toggle the first_empty
                first_empty = not first_empty
            else: # end of potential important list
                # check to see if the list has at least 7 elements **This may exclude the last page employees
                if (len(temp_list) < 7):
                    temp_list = []
                else:  # keep the data!!!
                    if (choice == 1):
                        employee_list.extend(temp_list)
                        temp_list = []
                        choice = 2
                    elif (choice == 2):
                        #may contain page number on the bottom!!!
#                         print temp_list
                        test = temp_list[-1]
                        if (("Page" in test) or ("PAGE" in test)):
                            temp_list = temp_list[:-1]
                        position_list.extend(temp_list)
                        temp_list = []
                        choice = 3
                    elif (choice == 3):
                        # salary MIGHT have a 'Base Pay in it' so take that out!
                        if (('BASE PAY' in temp_list[0]) or ('Base Pay'in temp_list[0])):  #because other years may have non-capitalized
                            temp_list = temp_list[1:]
                        salary_list.extend(temp_list)
                        temp_list = []
                        choice = 1
                    else:
                        print ("Error")
                              
        else: # if the line is not empty, add it to the temp_list
            temp_list.append(line)
            

    #NEED to convert all the salary in strings to a decimal object!
    #Store as a new array salary_float[]!!
    salary_float = []
    for i in range(len(salary_list)):
        try:
            salary = salary_list[i][1:]
            salary_float.append(float(salary.replace(",",""))) 
        except:     #if you can't convert it to float, it is unpaid leave!
            salary_float.append("")

            
    ############ Create the dataframe & return it! #######################        
    data = zip(employee_list, position_list, salary_list, salary_float)
    df = pd.DataFrame(data, columns=["Employee Name", "Position", "Salary", "Salary_Float"])
    return df

