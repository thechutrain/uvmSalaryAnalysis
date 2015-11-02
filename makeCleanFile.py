####
# this will take the raw file names and convert it to a clean version

# import re

def makeCleanFile(raw_file):
	lines = [line.rstrip('\n') for line in open(raw_file)]

	#clean file name
	clean = "clean_"
	raw_file = raw_file.replace("Data/", "")
	clean_fileName = clean + raw_file
	# print clean_fileName
	clean_file = open(clean_fileName, "w")

	#make a list of things I don't want to have in my file
	junk_str = ["= currently on", "THE UNIVERSITY OF VERMONT LIST OF BASE PAY", "PRIMARY JOB TITLE", "BASE PAY", "on the basis of a number of factors",
	"Release Date:", "* Base pay is ", "positions; ", "NAME"]
	#Read through each line!!
	# page = ["P", "a", "g", "e", " "]
	for line in lines:
		skip = False
		for x in range(len(junk_str)):
			if (junk_str[x] in line):
				skip = True
		## Special edit of Page, because there are some people named Page!!
		# if (bool(re.search(line, "/[P][a][g][e][\s][1-9]/"))):
		# 	print line
			# skip = True
		###
		## VERY MESSY - but it gets the job done. Having an error when importing re
		if (len(line) >= 5):
			if ((line[0]=="P") and (line[1]=="a") and (line[2]=="g") and (line[3]=="e") and (line[4]==" ")):
				skip = True
		# if (len(line) >= 5))
		# 	for y in range(len(page)):
		# 		if ((line[y]==page[y])):
		# 			pass
		# 		else:
		# 			skip = True
		if (skip == False):
			clean_file.write(line)
			clean_file.write("\n")
	#close the file
	clean_file.close()


makeCleanFile("Data/sr06.txt")