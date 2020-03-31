#importing libraries
from collections import Counter

def repetition(numbers):
    return Counter(numbers)

#declaring freq dictionary
if __name__ == "__main__":
    
    numbers = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
    freq = repetition(numbers)

#loop to print to print the number of times each value is occuring    
    for number, nooftimes in freq.items():
        print (number, "-", nooftimes)
        
