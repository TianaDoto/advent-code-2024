
def readFile(path):
    col1 = []
    col2 = []

    with open(path, 'r') as file:
        for line in file:
            
            parts = line.strip().split()
            if len(parts) == 2:  
                col1.append(parts[0])
                col2.append(parts[1])
    return col1, col2

def getMinIndex(arr):
    minim = min(arr)
    index = arr.index(minim)
    return int(minim), index


file_path = "/Users/FHRN01241/Documents/advent-code-2024/day 1/input 1.txt"
arr1, arr2 = readFile(file_path)

sum = 0
while(len(arr1) > 0):
    min1, index1 = getMinIndex(arr1)
    min2, index2 = getMinIndex(arr2)

    sum += abs(min1 - min2)
    arr1.pop(index1)
    arr2.pop(index2)

print(sum)
