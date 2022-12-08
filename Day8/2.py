import functools

def isTreeVisible(col, row, forest):
    leftVisible = 0
    for i in range(col-1,-1,-1):
        leftVisible += 1
        if forest[row][i] >= forest[row][col]:
            break
        
    rightVisible = 0
    for i in range(col+1, len(forest[0])):
        rightVisible += 1
        if forest[row][i] >= forest[row][col]:
            break
        
    topVisible = 0
    for i in range(row-1, -1, -1):
        topVisible += 1
        if forest[i][col] >= forest[row][col]:
            break

    downVisible = 0
    for i in range(row+1, len(forest)):
        downVisible += 1
        if forest[i][col] >= forest[row][col]:
            break
        
    return leftVisible*rightVisible*topVisible*downVisible


data = open('Day8/data_example.txt', 'r')
forest = []

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    forest.append(list(map(int, list(line))))

treeVisibility = []
for row in range(len(forest)):
    for col in range(len(forest[0])):
        treeVisibility.append(isTreeVisible(col, row, forest))

print(max(treeVisibility))
