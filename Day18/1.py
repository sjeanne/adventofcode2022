import functools
import numpy as np

def adjaceantDrop(lavaDrops, drop):
    nbAdj = 0
    adjVectors = [np.array([-1,0,0]), np.array([1,0,0]), np.array([0,-1,0]), np.array([0,1,0]), np.array([0,0,-1]), np.array([0,0,1])]
    for adj in adjVectors:
        if list(drop + adj) in lavaDrops:
            nbAdj += 1
    return nbAdj

data = open('Day18/data.txt', 'r')

lavaDrops = []
while True:

    line = data.readline().strip()
    if not line:
        break
    pass

    lavaDrops.append( list(map(int,line.split(','))))


sumFreeSide = 0
for drop in lavaDrops:
    print(drop, adjaceantDrop(lavaDrops, drop))
    sumFreeSide += 6 - adjaceantDrop(lavaDrops, drop)

print("Free side:", sumFreeSide)

