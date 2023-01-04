inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()
elvesCalories = 0
maxElvesCalories = 0

for line in fileLines:
    if line.startswith('\n'):
        if elvesCalories > maxElvesCalories:
            maxElvesCalories = elvesCalories
        elvesCalories = 0
    else:
        elvesCalories = elvesCalories + int(line)

print(maxElvesCalories)
