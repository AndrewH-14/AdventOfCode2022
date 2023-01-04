inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()
score = 0

for line in fileLines:
    if line[0] == 'A': # Rock
        if line[2] == 'X': # Rock (Tie)
            score = score + 4
        elif line[2] == 'Y': # Paper (Win)
            score = score + 8
        elif line[2] == 'Z': # Scissors (Lose)
            score = score + 3
    elif line[0] == 'B': # Paper
        if line[2] == 'X': # Rock (Lose)
            score = score + 1
        elif line[2] == 'Y': # Paper (Tie)
            score = score + 5
        elif line[2] == 'Z': # Scissors (Win)
            score = score + 9
    elif line[0] == 'C': # Scissors
        if line[2] == 'X': # Rock (Win)
            score = score + 7
        elif line[2] == 'Y': # Paper (Lose)
            score = score + 2
        elif line[2] == 'Z': # Scissors (Tie)
            score = score + 6

print(score)