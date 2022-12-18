import functools



data = open('Day14/data.txt', 'r')

cave = []

while True:

    line = data.readline().strip()
    if not line:
        break
    pass

    line = line.split(' -> ')
    prev = list(map(int,line[0].split(',')))

    cave.append(prev)
    for point in line[1:]:
        nextPoint = list(map(int,point.split(',')))
        cave.append(nextPoint)
        if nextPoint[0] == prev[0]:
            for y in range(min(nextPoint[1], prev[1]),max(nextPoint[1], prev[1])):
                if not([nextPoint[0],y] in cave):
                    cave.append([nextPoint[0],y])
        else:
            for x in range(min(nextPoint[0], prev[0]),max(nextPoint[0], prev[0])):
                if not([x,nextPoint[1]] in cave):
                    cave.append([x,nextPoint[1]])
        prev = nextPoint
        
sand = [500,0]
nbSand = 1
sandFlow = True
while sandFlow:
    if not([sand[0], sand[1]+1] in cave):
        sand = [sand[0], sand[1]+1]
    elif not([sand[0]-1, sand[1]+1] in cave):
        sand = [sand[0]-1, sand[1]+1]
    elif not([sand[0]+1, sand[1]+1] in cave):
        sand = [sand[0]+1, sand[1]+1]
    else:
        print(nbSand, sand)
        cave.append(sand)
        sand = [500,0]
        nbSand += 1

    sandFlow = sand[1] < 500
