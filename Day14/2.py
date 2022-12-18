import functools



data = open('Day14/data.txt', 'r')

cave = [ [0]*1000 for i in range(200)]

print(len(cave), len(cave[0]))

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
        cave[nextPoint[1]][nextPoint[0]] = 1
        if nextPoint[0] == prev[0]:
            for y in range(min(nextPoint[1], prev[1]),max(nextPoint[1], prev[1])):
                cave[y][nextPoint[0]] = 1
        else:
            for x in range(min(nextPoint[0], prev[0]),max(nextPoint[0], prev[0])):
                cave[nextPoint[1]][x] = 1
        prev = nextPoint



lowestAltitude = 0
for i in range(0,len(cave)):
    if 1 in cave[i]:
        lowestAltitude = i

lowestAltitude += 2

print("lowestAltitude", lowestAltitude)


for i in range(0,900):
    cave[lowestAltitude][i] = 1


sand = [0,500]
nbSand = 0
while cave[0][500] == 0:
    if cave[sand[0]+1][sand[1]] == 0:
        sand = [sand[0] + 1, sand[1]]
    elif cave[sand[0]+1][sand[1]-1]  == 0:
        sand = [sand[0]+1,sand[1]-1]
    elif cave[sand[0]+1][sand[1]+1]  == 0:
        sand = [sand[0]+1, sand[1]+1]
    else:
        print(nbSand, sand)  
        cave[sand[0]][sand[1]] = 1
        sand = [0,500]
        nbSand += 1


print(nbSand)