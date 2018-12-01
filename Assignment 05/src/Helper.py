

def DeepCopyList(listObject):
    return [item for item in listObject]

def GetDistance(latitude1, longitude1, latitude2, longitude2):
    # Manhattan
    #return abs(latitude1 - latitude2) + abs(longitude1 - longitude2)

    # Eucledean
    return ((latitude1 - latitude2)**2 + (longitude1 - longitude2)**2)**(1/2)