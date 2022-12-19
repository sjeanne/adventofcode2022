import functools
import numpy as np

def adjaceantDrop(lavaDrops, drop):
    nbAdj = 0
    adjVectors = [np.array([-1,0,0]), np.array([1,0,0]), np.array([0,-1,0]), np.array([0,1,0]), np.array([0,0,-1]), np.array([0,0,1])]
    for adj in adjVectors:
        if list(drop + adj) in lavaDrops:
            nbAdj += 1
    return nbAdj

def adjaceantDropWithoutEmpty(lavaDrops, wholeSpace ,drop):
    nbAdj = 0
    adjVectors = [np.array([-1,0,0]), np.array([1,0,0]), np.array([0,-1,0]), np.array([0,1,0]), np.array([0,0,-1]), np.array([0,0,1])]
    for adj in adjVectors:
        if list(drop + adj) in lavaDrops or (list(drop + adj) in wholeSpace):
            nbAdj += 1
    return nbAdj

data = open('Day18/data.txt', 'r')

lavaDrops = []
wholeSpace = []
spaceSize = 21
for x in range(0,spaceSize+1):
    for y in range(0,spaceSize+1):
        for z in range(0,spaceSize+1):
            wholeSpace.append([x,y,z])

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    drop = list(map(int,line.split(',')))
    lavaDrops.append( drop)
    wholeSpace.remove(drop)


for i in range(0,spaceSize+1):
    for j in range(0,spaceSize+1):
        for k in range(0,spaceSize+1):
            if [i,j,k] in lavaDrops:
                break
            wholeSpace.remove([i,j,k])

for i in range(0,spaceSize+1):
    for j in range(0,spaceSize+1):
        for k in range(0,spaceSize+1):
            if [i,k,j] in lavaDrops:
                break
            if [i,k,j] in wholeSpace:
                wholeSpace.remove([i,k,j])

for i in range(0,spaceSize+1):
    for j in range(0,spaceSize+1):
        for k in range(0,spaceSize+1):
            if [k,j,i] in lavaDrops:
                break
            if [k,j,i] in wholeSpace:
                wholeSpace.remove([k,j,i])

for i in range(spaceSize, -1, -1):
    for j in range(spaceSize, -1, -1):
        for k in range(spaceSize, -1, -1):
            if [i,j,k] in lavaDrops:
                break
            if [i,j,k] in wholeSpace:
                wholeSpace.remove([i,j,k])

for i in range(spaceSize, -1, -1):
    for j in range(spaceSize, -1, -1):
        for k in range(spaceSize, -1, -1):
            if [i,k,j] in lavaDrops:
                break
            if [i,k,j] in wholeSpace:
                wholeSpace.remove([i,k,j])

for i in range(spaceSize, -1, -1):
    for j in range(spaceSize, -1, -1):
        for k in range(spaceSize, -1, -1):
            if [k,j,i] in lavaDrops:
                break
            if [k,j,i] in wholeSpace:
                wholeSpace.remove([k,j,i])

sumFreeSide = 0
for drop in lavaDrops:
    print(drop, adjaceantDropWithoutEmpty(lavaDrops, wholeSpace, drop))
    sumFreeSide += 6 - adjaceantDropWithoutEmpty(lavaDrops, wholeSpace, drop)

print("Free side:", sumFreeSide)

