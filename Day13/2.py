import functools

RIGHT_ODER = 1
NOT_RIGHT_ORDER = -1
ORDER_NOT_DEFINED = 0

def splitPacket(packetStr):
    output = []
    packetStr = packetStr[1:-1]

    while len(packetStr) > 0:
        if packetStr[0] != '[':
            sepPos = packetStr.find(',')
            if sepPos != -1:
                output.append(packetStr[0:sepPos])
                packetStr = packetStr[sepPos+1:]
            else:
                output.append(packetStr)
                packetStr = ''
        else:
            nbOpenBrackets = 1
            cursor = 0
            while nbOpenBrackets > 0:
                cursor += 1
                if packetStr[cursor] == '[':
                    nbOpenBrackets += 1
                elif packetStr[cursor] == ']':
                    nbOpenBrackets -= 1
            output.append(packetStr[0:cursor+1])
            packetStr = packetStr[cursor+2:]
    
    return output

def isElementNumber(element):
    try:
        int(element)
        return True
    except:
        return False
        
def elementToList(element):
    if isElementNumber(element):
        return [element]
    else:
        return splitPacket(element)

def listCorrectlyOrdered(list1, list2):
    for i in range(len(list1)):

        if i >= len(list2):
            return NOT_RIGHT_ORDER

        if isElementNumber(list1[i]) and isElementNumber(list2[i]) :
            if int(list1[i]) > int(list2[i]):
                return NOT_RIGHT_ORDER
            elif int(list1[i]) < int(list2[i]):
                return RIGHT_ODER
            else:
                continue
        

        subListorder = listCorrectlyOrdered(
            elementToList(list1[i]),
            elementToList(list2[i]))
        if subListorder == ORDER_NOT_DEFINED:
            continue
        else:
            return subListorder

    if len(list1) == len(list2):
        return ORDER_NOT_DEFINED
    return RIGHT_ODER

data = open('Day13/data.txt', 'r')

listOfPakets = []
while True:

    line1 = data.readline().strip()
    if not line1:
        break
    pass

    line2 = data.readline().strip()
    data.readline() #empty

    listOfPakets.append( splitPacket(line1))
    listOfPakets.append( splitPacket(line2))

listOfPakets.append(['[2]'])
listOfPakets.append(['[6]'])

cursor = 0
while cursor < len(listOfPakets) - 1:
    if listCorrectlyOrdered(listOfPakets[cursor], listOfPakets[cursor+1]) != RIGHT_ODER:
        tmp = listOfPakets[cursor]
        listOfPakets[cursor] = listOfPakets[cursor+1]
        listOfPakets[cursor+1] = tmp
        cursor = 0
    else:
        cursor += 1

for i in range(0,len(listOfPakets)):
    print(i+1, listOfPakets[i])
