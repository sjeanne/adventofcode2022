import functools


def findCommonItem(bag1, bag2, bag3):
    for item in bag1:
        if bag2.find(item) != -1 and bag3.find(item) != -1:
            return item
    return ''

def itemPoint(item):
    if( 'a' <= item):
        return ord(item) - ord('a') + 1
    return ord(item) - ord('A') + 27

data = open('Day3/1_data.txt', 'r')

itemsPriority = 0
while True:
    bag1 = data.readline().strip()
    if not bag1:
        break
    pass

    bag2 = data.readline().strip()
    bag3 = data.readline().strip()

    commonItem = findCommonItem(bag1, bag2, bag3)
    itemsPriority += itemPoint(commonItem)
    print("{}".format(commonItem))

print("{}".format(itemsPriority))

