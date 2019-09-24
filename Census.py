#Read text file into a Python list
def createDataList():
    filename = "Economic_Data_2010.txt"
    file = open(filename,'r')
    dataList = []
    for record in file.readlines():
        fields = record.split(',')
        dataList.append(fields)
    file.close()
    return dataList


def getRegion():
    region = input("Please enter region:")
    region = lookupRegion(region)

    while region==False:
        region = input("'" + region+ "'"+ "was not found. Pls enter another region.")
    return region

def lookupRegion(region):
    """Looks up region in data file."""
    dataList = createDataList()
    for record in dataList:
        if(record[1] == region ):
            return record[1]
    return False

def createRegionalPopulationDictionary(region):
    datalist = createDataList()
    populationDict = {}
    for record in datalist:
        if record[1]==region:
            populationDict[record[0]]=record[2]
    return populationDict


def getPopulation(region=None):
    dict = createRegionalPopulationDictionary(region)
    for record in dict:
        population += float(record[2])
      
    return population

#There is one record per state.
#Iterating over the data and counting how many times the region appears,
#   gives the number of states in a region
def getNumOfStatesByRegion(region):
    dataList = createDataList()
    count=0
    for record in dataList:
        if(record[1] == region):
           count+=1 
    return count





def getGDP(region=None):
    if region ==None:
        return 12894.973 
    else:
        return 1776.04

def getAvgRegionalPopulation(region):
    population = getPopulation(region)
    numOfStates = getNumOfStatesByRegion(region)
    return population/numOfStates
 






#This actually turns out to be a duplicate.
#Above in getNumberofStateByRegion() number of records that
#correspond to region are counted and there are as many records
#as there are states in the region
#def getNumOfStatesInRegion(region = None):
#    if region == None:
#        return 0
#    else:
#        #note:  A compound if statement could have been used, and would have been quicker and easier, 
#        #   but I wanted to learn this technique to substitute for a switch stmt.
#        #   Although, I may never use it because it's hard to read.
#        switcher = {
#            'Great_Lakes': great_lakes,
#            'Far_West': far_west,
#            'Mid_East': mid_east,
#            'New_England': new_england,
#            'Plains': plains,
#            'Rockey_Mountain':rocky_mountain,
#            'Southeast':southeast,
#            'Southwest':southwest
#        }
#        # Get the function from switcher dictionary
#        func = switcher.get(region, lambda: getNumOfStatesInRegion)
#        # Execute the function
#        return (func())

#def great_lakes():
#    return 5
#def far_west():
#    return 6
#def mid_east():
#    return 6
#def new_england():
#    return 6
#def plains():
#    return 7
#def rocky_mountain():
#    return 5
#def southeast():
#    return 12
#def southwest():
#    return 4    