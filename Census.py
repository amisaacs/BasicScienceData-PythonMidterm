def add(x,y):
    return x+y

def lookupRegion(region):
    """Looks up region in data file."""
    filename = "Economic_Data_2010.txt"
    file = open(filename,'r')
    for record in file.readlines():
        fields = record.split(',')
        print (fields[1])
        if(fields[1] == region):
            file.close()
            return fields[1]
    file.close()
    return False

def getRegion():
    region = input("Please enter region:")
    region = lookupRegion(region)

    while region==False:
        region = input("'" + region+ "'"+ "was not found. Pls enter another region.")
