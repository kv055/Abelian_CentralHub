import math
#function that deletes NaN values from a list that is filled with indicator data
def delNan(list):
    new_list = [item for item in list if not(math.isnan(item)) == True]
    return new_list
