import functools


def moveElement(index, elementList):
    element = elementList[index]
    elementList = elementList[0:index] + elementList[index+1:]
    elementList.insert((index+element["v"])%(len(elementList)), element)
    return elementList

def findIndexByPos(pos, elementList):
    for i in range(0,len(elementList)):
        if elementList[i]["p"] == pos:
            return i

def findIndexByValue(value, elementList):
    for i in range(0,len(elementList)):
        if elementList[i]["v"] == value:
            return i    


data = open('Day20/data.txt', 'r')

buffer = []

while True:

    line = data.readline().strip()
    if not line:
        break
    pass
    buffer.append({"v":int(line),"p":len(buffer)})

for i in range(0, len(buffer)):
    index = findIndexByPos(i,buffer)
    buffer = moveElement(index, buffer)

indexZero = findIndexByValue(0,buffer)
print(buffer[(indexZero+1000) % len(buffer)]["v"] + buffer[(indexZero+2000) % len(buffer)]["v"] + buffer[(indexZero+3000) % len(buffer)]["v"])