import bisect

inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()
elvesCalories = 0
listElvesCalories = []

for line in fileLines:
    if line.startswith('\n'):
        bisect.insort(listElvesCalories, elvesCalories)
        elvesCalories = 0
    else:
        elvesCalories = elvesCalories + int(line)

lengthOfList = len(listElvesCalories);
print(listElvesCalories[lengthOfList - 1] + listElvesCalories[lengthOfList - 2] + listElvesCalories[lengthOfList - 3])