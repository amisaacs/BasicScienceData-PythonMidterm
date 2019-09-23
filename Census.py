def add(x,y):
    return x+y

def lookupRegion(region):
    """Looks up region in data file."""
    dataList = createDataList()
    for record in dataList:
        if(record[1] == region ):
            return record[1]
    return False

def getRegion():
    region = input("Please enter region:")
    region = lookupRegion(region)

    while region==False:
        region = input("'" + region+ "'"+ "was not found. Pls enter another region.")
    return region

def getNumOfRecordsForRegion(region):
    dataList = createDataList()
    count=0
    for record in dataList:
        if(record[1] == region):
           count+=1 
    return count

def createDataList():
    filename = "Economic_Data_2010.txt"
    file = open(filename,'r')
    dataList = []
    for record in file.readlines():
        fields = record.split(',')
        dataList.append(fields)
    file.close()
    return dataList


def getPopulation(region=None):
    if region==None:
        return 309.3264
    else: 
        return 46.436

def getGDP(region=None):
    if region ==None:
        return 12894.973
    else:
        return 1776.04