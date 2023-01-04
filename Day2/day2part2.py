inputFile = open("input.txt", "r")
fileLines = inputFile.readlines()
score = 0

for line in fileLines:
    if line[0] == 'A': # Rock
        if line[2] == 'X': # Lose
            # Must play scissors to lose
            score = score + 3
        elif line[2] == 'Y': # Draw
            # Must play rock to draw
            score = score + 4
        elif line[2] == 'Z': # Win
            # Must play paper to win
            score = score + 8
    elif line[0] == 'B': # Paper
        if line[2] == 'X': # Lose
            # Must play rock to lose
            score = score + 1
        elif line[2] == 'Y': # Draw
            # Must play paper to draw
            score = score + 5
        elif line[2] == 'Z': # Win
            # Must play scissors to win
            score = score + 9
    elif line[0] == 'C': # Scissors
        if line[2] == 'X': # Lose
            # Must play paper to lose
            score = score + 2
        elif line[2] == 'Y': # Draw
            # Must play scissors to draw
            score = score + 6
        elif line[2] == 'Z': # Win
            # Must play rock to win
            score = score + 7

print(score)