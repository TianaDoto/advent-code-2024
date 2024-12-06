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

file_path = "/Users/FHRN01241/Documents/advent-code-2024/1/input 1.txt"
arr1, arr2 = readFile(file_path)

sum = 0
for i in arr1:
    count = 0
    for j in arr2:
        if(i == j):
            count += 1
    sum += count * int(i)

print(sum)