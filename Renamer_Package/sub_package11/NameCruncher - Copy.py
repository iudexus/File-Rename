### CSV File : "comma separated value"

#CSVs are commonly generated by exporting data from a spreadsheet
#or may be downloaded from the interned. You may also be able to
#download data from websites, into spreadsheets and from there, 
#export to a .csv

### Weather data analisis prog ###

## read in data ##
##open file
# get filename # the filename for this program is course8.csv
filename = input("Enter the name of the data file:")
# open file
infile = open(filename, "r")

datalist = []
#loop over data line by line
#data is read as a string
for xline in infile:
    date, high, low, rain = xline.split(".")    #get relevent data from string w/line.split() and assign a variable """"""
    lowtemp = int(low)
    hightemp = int(high)       #convert to appropriate values
    rainfall = float(rain)
    m, d, y = date.split("/")
    month = int(m)
    day = int(d)
    year = int(y)
    datalist.append([day, month, year, lowtemp, hightemp, rainfall])
    #store data in datalist


#close the file
infile.close()

#print(datalist)
## analyze data ## 

#get date from user
userinputm = int(input("What month should I analyze? "))
userinputd = int(input("What day should I investigate? "))
#find date in list
container = []
for event in datalist:
    if (event[0] == userinputd) and (event[1] == userinputm):
        container.append([event])
#analyze data
runningmin = 1000
runningmax = -1000
numgerdates =0
sumofmins = 0
sumofmaxx = 0

##loop thru data
for singleday in datalist:
    numgerdates += 1
    sumofmins += singleday[3]
    sumofmaxx += singleday[4]
    if singleday[3] < runningmin:
        runningmin = singleday[3]
    if singleday[4] > runningmax:
        runningmax = singleday[4]

avglo = sumofmins / numgerdates
avghi = sumofmaxx / numgerdates

#count num dates

#store max & min temps

#add max & min temps

##calc max & min


## present data ##

print("There were",numgerdates,"days analyzed")
print("The lowest temperature on record was", runningmin)
print("The highest temperature on record was", runningmax)
print("The average low has been", avglo)
print("The average high has been", avghi)



"""THE TRUE DAMN CODE, NINJA!"""

return