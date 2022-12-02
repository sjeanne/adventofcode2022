import functools
    

data = open('Day2/1_data.txt', 'r')

totalScore = 0

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    opponentMove, matchResult = line.split(' ')

    opMove = 0
    if opponentMove == 'A':
        opMove = 1
    elif opponentMove == 'B':
        opMove = 2
    elif opponentMove == 'C':
        opMove = 3

    if matchResult == 'X':
        opMove -= 1
        totalScore += 0
    elif matchResult == 'Y':
        totalScore += 3
    elif matchResult == 'Z':
        opMove += 1
        totalScore += 6

    if opMove == 0:
        opMove = 3
    if opMove == 4:
        opMove = 1

    totalScore += opMove


    print("#  score: {}".format(totalScore))                                                

print("# Final score: {}".format(totalScore))
