import functools

DATA_EXAMPLE = [
    ['Z','N'],
    ['M', 'C','D'],
    ['P']]
DATA = [
    ['B','Z','T'],
    ['V','H','T','D','N'],
    ['B','F','M','D'],
    ['T','J','G','W','V','Q','L'],
    ['W','D','G','P','V','F','Q','M'],
    ['V','Z','Q','G','H','F','S'],
    ['Z','S','N','R','L','T','C','W'],
    ['Z','H','W','D','J','N','R','M'],
    ['M','Q','L','F','D','S']]



data = open('Day5/1_data.txt', 'r')
crates = DATA

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    _, numToMove, _, fromColumn, _, toColumn = line.split(' ')
    numToMove = int(numToMove)
    fromColumn = int(fromColumn)-1
    toColumn = int(toColumn)-1

    while numToMove > 0:
        crates[toColumn].append(crates[fromColumn].pop())
        numToMove -= 1

for col in crates:
    print(col.pop())
