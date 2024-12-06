def readFile(path):
    rows = []

    with open(path, 'r') as file:
        for row in file:
            parts = row.strip().split()
            rows.append(parts)
    return rows

def checkIncrease(row):
    increase = False
    
    for i in range(len(row) - 1):
        if((row[i] < row[i + 1])):
            increase = True
        else:
            return False
    return increase

def checkDecrease(row):
    decrease = False

    for i in range(len(row) - 1):
        if(row[i] > row[i + 1]):
            decrease = True
        else:
            return False
    return decrease

def checkDiff(row):
    safe = False
    for i in range(len(row) - 1):
        if( 1 <= abs(int(row[i]) - int(row[i + 1])) <= 3):
            safe = True
        else:
            return False
    return safe


def checkSafe(row):
    if(checkIncrease(row) and checkDiff(row)):
        return True
    elif(checkDecrease(row) and checkDiff(row)):
        return True
    else:
        return False

filePath = "/Users/FHRN01241/Documents/advent-code-2024/day 2/input 2.txt"
rows = readFile(filePath)

rowsTmp = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9]
]

sum = 0
for row in rows:
    if(checkSafe(row)):
        sum += 1

print(sum)