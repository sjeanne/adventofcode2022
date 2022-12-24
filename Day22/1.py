import functools
import re

def turn(currentDir, rot):
    dirs = ['L','U','R','D']
    return dirs[(dirs.index(currentDir) + (1 if rot == 'R' else -1)) % 4]

def move(map, pos, direction):
    nextPos = [0,0]
    if direction == 'L':
        nextPos = [pos[0]-1, pos[1]]
        if nextPos[0] < 0 or map[nextPos[1]][nextPos[0]] == " ":
            nextCol = len(map[nextPos[1]]) - 1
            while map[nextPos[1]][nextCol] == " ":
                nextCol -= 1
            nextPos[0] = nextCol
    elif direction == 'R':
        nextPos = [pos[0]+1, pos[1]]
        if nextPos[0] >= len(map[nextPos[1]]) or map[nextPos[1]][nextPos[0]] == " ":
            nextPos[0] = re.search(r'[^ ]', map[nextPos[1]]).start()
    elif direction == 'U':
        nextPos = [pos[0], pos[1]-1]
        if nextPos[1] < 0 or map[nextPos[1]][nextPos[0]] == " ":
            nextRow = len(map) - 1
            while map[nextRow][nextPos[0]] == " ":
                nextRow -= 1
            nextPos[1] = nextRow
    elif direction == 'D':
        nextPos = [pos[0], pos[1]+1]
        if nextPos[1] >= len(map) or map[nextPos[1]][nextPos[0]] == " ":
            nextRow = 0
            while map[nextRow][nextPos[0]] == " ":
                nextRow += 1
            nextPos[1] = nextRow

    if '# '.find(map[nextPos[1]][nextPos[0]]) == -1:
        return nextPos
    else:
        return pos

data = open('Day22/data.txt', 'r')

mapping = []

while True:
    line = data.readline().strip("\n\r")
    if not line:
        break
    pass
    mapping.append(line)

largerRow = max(map(len, mapping))

print(" ".join(str(x) for x in map(len, mapping)))
mapping = list(map(lambda row: row + " "*(largerRow-len(row)), mapping))
print(" ".join(str(x) for x in map(len, mapping)))


pos = [mapping[0].find('.'),0]
direction = 'R'
command = re.split(r"(\D+)", data.readline().strip())

while len(command) > 0:
    steps = int(command.pop(0))
    while steps > 0:
        pos = move(mapping, pos, direction)
        steps -= 1
    if len(command) == 0:
        break
    direction = turn(direction, command.pop(0))

print(pos, direction)
print((pos[1] + 1)*1000 + 4 * (pos[0] + 1))