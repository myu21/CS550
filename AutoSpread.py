"""
Mitchell Yu
22 Feb 2019
Final Project - Solve a Problem
- Spending Spreadsheet automator
		The problem I chose to solve was my personal problem of making a spending spreadsheet. While I can pretty easily create one, it is tedious and time consuming, as I have to individually type in each value into each cell. It just takes so long and can honestly get really frustrating, especially since the task is so tedious it seemed as if it could be done by a robot, hence the goal of this project.
	Challenges
		The first issue was how to convert the data provided by the online banking website into a workable form, preferably in array form. At first I had trouble because I thought the only way to get the data was in pdf form, which was probablematic. Working with pdf is a pain in python, and most of the API's that do offer this functionality all cost money. I did however manage to extract the tabular data into what was essentially a giant string, which was almost impossible to work with. I later discovered that it was actually possible to download the data directly into CSV.
		The second challenge I faced was what the best form was for the data. I started the project by importing CSV using the Pandas library into a pandas array. I read a lot about how pandas was really good for data manipulation, exactly what I was looking for. I ended up completing half of my code before reaching a step where the pandas array ran out of flexability, so I decided to completely scrap pandas. Instead I imported CSV using the Numpy library into a numpy array. Then, I intertwined the usage of numpy array and stock python arrays. Numpy arrays are more "low-level", meaning that I had much more freedom with what I could do. While some of the solutions I used aren't the most elegant, it still gets the job done.
		The third issue probably was the worst of them all because I spent way too much time trying about every solution I could think of. I had a problem when transfering data from CSV into Numpy array. After trying about everything, it ended up just being a hashtag hiding in a long string in one of the cells. The solution was literally just one change in one parameter, making it both really infuriating and satisfying.
	Description
		Execution of the code is very anticlimactic, which is exactly what I was going for. My goal was to make the execution of my code completely seamless. The goal was to make the moment from downloading the data up until the creation of the excel file to be hands-free. Because of the way the code is designed, only three steps are required:
			- Download the CSV from the website onto the desktop
			- Run the code
			- Choose the type of spreadsheet (monthly or annual)
		It's that simple. There is no need to type down the file name, or choose its destination. It just runs by itself.
		Now this code isn't exactly generalized for all cases. I tailored it specifically for my own use. The problem with generalization is that there are too many differing factors. Other people might have different file name headers, or their banks may store data in a different format from mine. More importantly, the layout and features of a spreadsheet heavily depends on what a person needs.
		For me, persoanlly, all I need is my spending information in different catagories displayed in a nice way for my own reference. While it would be nice to find repositories of words that are related to each catagory, I really only need the words that are applicable to specifically what I spend my money on
		I would imagine that in the future, I would eventually get to integrate this spreadsheet into a greater dataset that would include things like rent, expenses, salary etc. 
Sources:
	- www.hexcolortool.com
	- xlsxwriter.readthedocs.io/index.html
On My Honor: Mitchell Yu
"""

import numpy as np
import datetime as dt
import xlsxwriter as xl



# Sorting data by date (by month or year, depending on type of spreadsheet choosen)

while True:
	daterange = input("Would you like a monthly (1) or yearly (2) spreadsheet?\n>>>")
	if int(daterange) < 1 or int(daterange) > 2:
		print("Sorry, that is not a valid input")
	else:
		break

current = str(dt.datetime.now()) # finds current time

data = np.genfromtxt("Chase6797_Activity_20"+str(current[2])+str(current[3])+str(current[5])+str(current[6])+str(current[8])+str(current[9])+".csv",delimiter=',',dtype=str, comments=None, skip_header=1) # finds filename based on the date (when downloading the file, its name will reflect the date that is was downloaded). Essentially just converting CSV data to a Numpy array
data = np.delete(data, 0, 1) # deleting top row (labels), as one cell holds a datatype python can't handle
data = np.delete(data, np.s_[6:], 1) # getting rid of useless data

datespecific = [] # transfers data from Numpy array into an array with only the data relating to the current month or year

if int(daterange) == 1:
	for x in range(len(data)):
		if data[x,0][0] == current[5] and data[x,0][1] == current[6]:
			datespecific.append(data[x,:])
else:
	for x in range(len(data)):
		if data[x,0][8] == current[2] and data[x,0][9] == current[3]:
			datespecific.append(data[x,:])



# Catagorizing the data
	# These are lists of words that commonly show up in the descriptions of the purchases that I make. If my buying habits were more diverse, then I would have considered in looking for an online repository of words related to a catagory, but there are pretty much three restaraunts within walking distance, so I don't see myself needing much more data than is below for catagorization.
subscriber = ["itunes", "spotify"]
subscribertotal = 0
food = ["food", "noodle", "chicken", "fried", "gas", "cheek", "restaraunt", "drink", "mr ds", "cafe ra", "wal-mart", "ralphs","sushi", "kitchen", "chef", "mcdonald's"]
foodtotal = 0
transport = ["lyft", "uber"]
transporttotal = 0
athletics = ["tennis", "gym", "cliffs of id", "climb", "adidas", "nike", "athletic", "running", "brace", "fitness", "stripe.com", "sports", "sender"]
athleticstotal = 0
music = ["vinyl", "trumpet", "mute", "music", "qrates", "hhv", "merchbar", "sleevecity", "jazz"]
musictotal = 0
ebay = ["paypal"]
ebaytotal = 0
withdraw = ["atm", "withdraw", "non-chase"]
withdrawtotal = 0
exempt = ["online transfer from"]
othertotal = 0

for x in range(len(datespecific)):
	if any(word in datespecific[x][1].lower() for word in subscriber): # tests if a word relating to a catagory shows up in the item/service description
		subscribertotal += -1*float(datespecific[x][-4]) # if so, the cost is added to the total catagory spending
		datespecific[x][-3] = "subscriber" # the purchace is then marked by its catagory
		datespecific[x][-1] = 0 # marking the purchace with the colorcode of its catagory
	elif any(word in datespecific[x][1].lower() for word in food):
		foodtotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "food"
		datespecific[x][-1] = 1
	elif any(word in datespecific[x][1].lower() for word in transport):
		transporttotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "transport"
		datespecific[x][-1] = 2
	elif any(word in datespecific[x][1].lower() for word in athletics):
		athleticstotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "athletics"
		datespecific[x][-1] = 3
	elif any(word in datespecific[x][1].lower() for word in music):
		musictotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "music"
		datespecific[x][-1] = 4
	elif any(word in datespecific[x][1].lower() for word in ebay):
		ebaytotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "ebay"
		datespecific[x][-1] = 5
	elif any(word in datespecific[x][1].lower() for word in withdraw):
		withdrawtotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "withdraw"
		datespecific[x][-1] = 6
	elif any(word in datespecific[x][1].lower() for word in exempt):
		datespecific[x][-3] = "n/a"
		datespecific[x][-1] = 8
	else:
		othertotal += -1*float(datespecific[x][-4])
		datespecific[x][-3] = "other"
		datespecific[x][-1] = 7



# Setting up excel spreadsheet

if float(daterange) == 1:
	titletext = str(current[5])+str(current[6])
else:
	titletext = "ANNUAL"
workbook = xl.Workbook('20'+str(current[2])+str(current[3])+'_'+titletext+'_SPENDING_SPREADSHEET.xlsx') # creates excel file named after the date range it covers as well as the spreadsheet type
worksheet = workbook.add_worksheet()



# Formatting cells with boldness and color

title_format = workbook.add_format({'bold': True}) # title format, just a simple plain bold
catagory = ["subscriber", "food", "transport", "athletics", "music", "ebay", "withdraw", "other"]
colorsaturated = ['#EC99F6', '#FF83A2', '#F2AD8E', '#FFEB99', '#74FF9B', '#4DE8C4', '#8B9DFF', '#0367A6']
colorlight = ['#F7D5FB', '#FFC7D5', '#F8D1BF', '#FFF6D1', '#B8FFCC', '#AEF4E4', '#CCD4FF', '#55BCFC', 'FFFFFF']
colorsat = {} # dictionary for the colors of the catagory headers
colorlit = [] # list for the lighter colors of the items themselves
for x in range(1,9):
	colorsat["{0}".format(catagory[x-1])] = workbook.add_format({'bg_color':colorsaturated[x-1], 'bold': True})
for y in range(1,10):
	colorlit.append(workbook.add_format({'bg_color':colorlight[y-1]}))



# Adding data to spreadsheet

for z in range(len(datespecific)): # putting data into cells, along with their formatting
	worksheet.write(z+1, 0, datespecific[z][0])
	worksheet.write(z+1, 1, datespecific[z][1], colorlit[int(datespecific[z][-1])])
	worksheet.write(z+1, 2, float(datespecific[z][2]), colorlit[int(datespecific[z][-1])])
	worksheet.write(z+1, 3, float(datespecific[z][4]), colorlit[int(datespecific[z][-1])])
	worksheet.write(z+1, 4, datespecific[z][3], colorlit[int(datespecific[z][-1])])

titlenames = ["Date", "Description", "Cost", "Balance", "Type", "", "Totals"] # creating the titles of the spreadsheet
for x in range(6):
	worksheet.write(0, x, titlenames[x], title_format)
for y in range(1,9):
	worksheet.write(y, 6, catagory[y-1], colorsat[catagory[y-1]])
# inserting the totals for each catagory
worksheet.write(1, 7, subscribertotal)
worksheet.write(2, 7, foodtotal)
worksheet.write(3, 7, transporttotal)
worksheet.write(4, 7, athleticstotal)
worksheet.write(5, 7, musictotal)
worksheet.write(6, 7, ebaytotal)
worksheet.write(7, 7, withdrawtotal)
worksheet.write(8, 7, othertotal)

worksheet.write(10, 6, "Total", title_format)
worksheet.write(10, 7, '=SUM(H2:H9)') # sum all purchases
worksheet.write(11, 6, "Balance", title_format)
worksheet.write(11, 7, float(datespecific[0][4]))

worksheet.set_column('B:B', 30) # widen description cells

workbook.close()