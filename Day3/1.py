import functools


def findCommonItem(list1, list2):
    for item in leftPocket:
        if rightPocket.find(item) != -1:
            return item
    return ''

def itemPoint(item):
    if( 'a' <= item):
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27

data = open('Day3/1_data.txt', 'r')

itemsPriority = 0
while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    leftPocket = line[:len(line)//2]
    rightPocket = line[len(line)//2:]
    commonItem = findCommonItem(leftPocket, rightPocket)
    itemsPriority += itemPoint(commonItem)

print("{}".format(itemsPriority))

