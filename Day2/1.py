import functools
    

data = open('Day2/1_data_example.txt', 'r')

totalScore = 0

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    opponentMove, myMove = line.split(' ')

    if myMove == 'X':
        totalScore += 1
    elif myMove == 'Y':
        totalScore += 2
    elif myMove == 'Z':
        totalScore += 3

    if (opponentMove == 'A' and myMove == 'X') or (opponentMove == 'B' and myMove == 'Y') or (opponentMove == 'C' and myMove == 'Z'):
        totalScore += 3
    if opponentMove == 'A' and myMove == 'Y':
        totalScore += 6
    if opponentMove == 'B' and myMove == 'Z':
        totalScore += 6
    if opponentMove == 'C' and myMove == 'X':
        totalScore += 6        

    print("#  score: {}".format(totalScore))                                                

print("# Final score: {}".format(totalScore))
