from rawFile_to_pandaDf import rawFile_to_pandaDf

def analyzeAllYears():
    list_fileNames = ["sr96.txt", "sr97.txt", "sr98.txt", "sr99.txt", "sr00.txt", "sr01.txt", "sr02.txt", "sr03.txt", "sr04.txt", "sr05.txt", "sr06.txt", "sr07.txt", "sr08.txt", "sr09.txt", "sr10.txt", "sr11.txt","sr12.txt", "sr13.txt", "sr14.txt"]
    file_dir = "rawData_txt/"      # this is the directory the raw data is in
    All_Data_Dict = {}
    for i in range(len(list_fileNames)):
        name = list_fileNames[i].replace("sr","DataYear_")
        name = name.replace(".txt", "")
#         print name
        dataframe = rawFile_to_pandaDf(file_dir + list_fileNames[i])
        All_Data_Dict[name] = dataframe
    return All_Data_Dict
    

data = analyzeAllYears()


##### TESTING! ######
example = "DataYear_00"
print data[example]
print "data from %s" % example