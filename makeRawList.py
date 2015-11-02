###################################################################
# This function will make a dictionary containing lists (employee, position, salary)
# and accepts the raw_file name in the argument


################## IMPORT Statements ###############################
import pprint
import pandas as pd
from makeCleanFile import makeCleanFile

################### sep_rawFile_to_panda_df() ############################
def makeRawList(raw_file):
    # see if filename is a string
    if (type(raw_file) != str):
        print("Error! Filename must be a string")
        # exit here? 
    else:
        pass

    ############ ADDING makeCleanFile function ##############
    clean_file = makeCleanFile(raw_file) #assumes that the raw_file is in Data/


    # # create a new filename that is clean_filename 
    lines = [line.rstrip('\n') for line in open(clean_file)]
    
    ############
    prev_empty = True
    temp_list = []       # temporary list that holds data
    employee_list = []   # employee names
    position_list = []   # holds the position of employees
    salary_list = []     # holds all the salaries
    column_num = 1
    for line in lines:
        if (line == ""):
            if (prev_empty == False):
                #enter the temp_list into each list:
                if (column_num == 1):
                    #enter into name
                    employee_list.extend(temp_list)
                    prev_empty = True
                    temp_list = []
                    column_num = 2
                elif (column_num == 2):
                    #enter into position
                    position_list.extend(temp_list)
                    prev_empty = True
                    temp_list = []
                    column_num = 3
                elif (column_num == 3):
                    #enter into postion
                    salary_list.extend(temp_list)
                    prev_empty = True
                    temp_list = []
                    column_num = 1
                else:
                    print "problems"
            else:
                prev_empty = True
                temp_list = [] # reset the temp list
        else:
            temp_list.append(line)
            prev_empty = False            

    salary_float = []
    for i in range(len(salary_list)):
        try:
            salary = salary_list[i][1:]
            salary_float.append(float(salary.replace(",",""))) 
        except:     #if you can't convert it to float, it is unpaid leave!
            salary_float.append(0)

#     ###### CREATE A DICTIONARY that contains everything I want to return! ######
    return_dict = {}
    return_dict["salary_list"] = salary_list
    return_dict["employee_list"] = employee_list
    return_dict["position_list"] = position_list
    return_dict["salary_float"] = salary_float
    return return_dict    

        ##### DEBUGGING ########
    # last_e = len(employee_list) - 1
    # last_s = len(salary_list) - 1
    # last_p = len(position_list) - 1 
    # print employee_list[last_e]
    # print salary_list[last_s]
    # print position_list[last_p]
    # print len(employee_list)
    # print len(salary_list)
    # print len(position_list)
    # print employee_list[1000]
    # print salary_list[1000]
    # print position_list[1000]
#### CALLING THE FUNCTION #####
# d = makeRawList("Data/sr12.txt")
# pprint.pprint(d)