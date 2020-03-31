def totalCost(myList):
    
    sum = 0
    for i in myList:
        sum = sum + myList[i]
    return sum

list = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35, "Wayne": 45, "Thomas": 58}
print("Total amount:", totalCost(list))
