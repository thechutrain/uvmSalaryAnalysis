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

    # ### Organize the lines into temporary lists and append them to the 3 separate lists
    # first_empty = True   # boolean that toggles to see if its firsttime its empty
    # temp_list = []       # temporary list that holds data
    # employee_list = []   # employee names
    # position_list = []   # holds the position of employees
    # salary_list = []     # holds all the salaries
    # choice = 1

    # # pprint.pprint(lines)
    # count = 0
    # start_check = False
    # list_count = 1
    # temp_list = []
    # # cont = True
    # while (cont):
    #     for line in lines:
    #     ### First if is look for the page opening string!
    #         str_match = '\x0cTHE UNIVERSITY OF VERMONT LIST OF BASE PAY*'
    #         if (line == str_match):
    #             count = 0
    #             # print line
    #         elif ((count == 7) and (start_check==False)):
    #             start_check = True;
    #             # clean up temp list
    #             temp_list = []

    #         ### If check is True, look through the next three columns:
    #         if (start_check):
    #             ### Three options here - employee, position, or salary
    #             if (list_count == 1):
    #                 #code
    #                 if (line == ""):
    #                     list_count = 2
    #                 else:
    #                     employee_list.append(line)

    #             elif (list_count ==2):
    #                  #code
    #                 if (line == ""):
    #                     list_count = 3
    #                 else:
    #                     position_list.append(line)
    #             elif (list_count == 3):
    #                 #code
    #                 if (line == ""):
    #                     list_count = 1
    #                     start_check = False
    #                     cont = False
    #                 else:
    #                     salary_list.append(line)
    #             else:
    #                 print ("You messed up!!!!!!!")
    #         ## Counter for each line, resetted after each opening header    
    #         count +=1

    #####################
    # Does not work!
    # for line in lines:
    #     ### First if is look for the page opening string!
    #     str_match = '\x0cTHE UNIVERSITY OF VERMONT LIST OF BASE PAY*'
    #     if (line == str_match):
    #         count = 0
    #         # print line
    #     elif ((count == 7) and (start_check==False)):
    #         start_check = True;
    #         # clean up temp list
    #         temp_list = []

    #     ### If check is True, look through the next three columns:
    #     if (start_check):
    #         ### Three options here - employee, position, or salary
    #         if (list_count == 1):
    #             #code
    #             if (line == ""):
    #                 list_count = 2
    #             else:
    #                 employee_list.append(line)

    #         elif (list_count ==2):
    #              #code
    #             if (line == ""):
    #                 list_count = 3
    #             else:
    #                 position_list.append(line)
    #         elif (list_count == 3):
    #             #code
    #             if (line == ""):
    #                 list_count = 1
    #                 start_check = False
    #             else:
    #                 salary_list.append(line)
    #         else:
    #             print ("You messed up!!!!!!!")
    #     ## Counter for each line, resetted after each opening header    
    #     count +=1


### OLD CODE - something is not working here; I'm missing people    
#     for line in lines:
#         if (line == ''):  #checks to see if line is empty
#             #check to see if first empty
#             if (first_empty):     # if it is the first empty, pass & toggle the first_empty
#                 first_empty = not first_empty
#             else: # end of potential important list
#                 # check to see if the list has at least 7 elements **This may exclude the last page employees
#                 if (len(temp_list) < 7):
#                     temp_list = []
#                 else:  # keep the data!!!
#                     if (choice == 1):
#                         employee_list.extend(temp_list)
#                         temp_list = []
#                         choice = 2
#                     elif (choice == 2):
#                         #may contain page number on the bottom!!!
# #                         print temp_list
#                         test = temp_list[-1]
#                         if (("Page" in test) or ("PAGE" in test)):
#                             temp_list = temp_list[:-1]
#                         position_list.extend(temp_list)
#                         temp_list = []
#                         choice = 3
#                     elif (choice == 3):
#                         # salary MIGHT have a 'Base Pay in it' so take that out!
#                         if (('BASE PAY' in temp_list[0]) or ('Base Pay'in temp_list[0])):  #because other years may have non-capitalized
#                             temp_list = temp_list[1:]
#                         salary_list.extend(temp_list)
#                         temp_list = []
#                         choice = 1
#                     else:
#                         print ("Error")
                              
#         else: # if the line is not empty, add it to the temp_list
#             temp_list.append(line)
            

#     #NEED to convert all the salary in strings to a decimal object!
#     #Store as a new array salary_float[]!!
#     salary_float = []
#     for i in range(len(salary_list)):
#         try:
#             salary = salary_list[i][1:]
#             salary_float.append(float(salary.replace(",",""))) 
#         except:     #if you can't convert it to float, it is unpaid leave!
#             salary_float.append("")

#     ###### CREATE A DICTIONARY that contains everything I want to return! ######
#     return_dict = {}
#     return_dict["salary_list"] = salary_list
#     return_dict["employee_list"] = employee_list
#     return_dict["position_list"] = position_list
#     return_dict["salary_float"] = salary_float
#     return return_dict    

        ##### DEBUGGING ########
    # last_e = len(employee_list) - 1
    # last_s = len(salary_list) - 1
    # last_p = len(position_list) - 1 
    # print employee_list[last_e]
    # print salary_list[last_s]
    # print position_list[last_p]
    print len(employee_list)
    print len(salary_list)
    print len(position_list)
    print employee_list[1000]
    print salary_list[1000]
    print position_list[1000]
#### CALLING THE FUNCTION #####
makeRawList("Data/sr12.txt")
# r = makeRawList("Data/sr06.txt")
# print r       # Don't Do it, its gonna be a lot!