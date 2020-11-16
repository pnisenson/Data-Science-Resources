###USE THIS FILE AS A QUICK REFERENCE TO READ AND WRITE CSV FILES###

# import libraries
import os
import csv

# identify csv file to use
csvfile = os.path.join('File Folder','file2read.csv')

# apply csv reader to file
with open(csvfile) as file_name:
	file_name = csv.reader(file_name, delimiter = ",")
# identify header row
	csvheader = next(file_name)

-----------------------------------------------------------------------------------------
# create lists to write to file as rows of data
	col1data = ["Name1","Name2","Name3"]
	col2data = [20, 30, 40]
	col3data = ["Accountant", "Coder", "Librarian"]

# zip user data together
	user_data = zip(col1data, col2data, col3data)

# use for loop to create report list in which each zipped detail is its own sublist
	report = []
	for x in user_data:
		report.append(x)

# develop output path to write analysis.txt in the Analysis folder
output_path = os.path.join("Analysis","analysis.txt")

# open the output file in write mode. Default delimeter is comma
with open(output_path, "w", newline = '') as datafile:
	writer = csv.writer(datafile)
# to create header row
	writer.writerow(['user','age','job'])
# write file with each user's data as a row
	writer.writerows(report)
# create row with any miscellaneous info using commas to seperate the columns
	writer.writerow(['random message xyz','', 'hello'])
# create blank row
	writer.writerow([])
