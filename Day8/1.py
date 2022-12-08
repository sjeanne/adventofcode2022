import functools

def isTreeVisible(col, row, forest):
    allNeighboors = []
    for i in range(col):
        allNeighboors.append(forest[row][i])
    if max(allNeighboors) < forest[row][col]:
        return True
        
    allNeighboors = []
    for i in range(col+1, len(forest[0])):
        allNeighboors.append(forest[row][i])
    if max(allNeighboors) < forest[row][col]:
            return True
        
    allNeighboors = []
    for i in range(row):
        allNeighboors.append(forest[i][col])
    if max(allNeighboors) < forest[row][col]:
        return True
        
    allNeighboors = []
    for i in range(row+1, len(forest)):
        allNeighboors.append(forest[i][col])
    if max(allNeighboors) < forest[row][col]:
        return True
        
    return False


data = open('Day8/data.txt', 'r')
forest = []

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    forest.append(list(map(int, list(line))))

visibleTrees = 0
for row in range(len(forest)):
    for col in range(len(forest[0])):
        if row == 0 or row == len(forest)-1:
            visibleTrees += 1
            continue
        if col == 0 or col == len(forest[0])-1:
            visibleTrees += 1
            continue
        if isTreeVisible(col, row, forest):
            visibleTrees += 1
            print(row, col)

print("Visible trees", visibleTrees)
