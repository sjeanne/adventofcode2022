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
            print(">False right list shorter", len(list1), len(list2))
            return NOT_RIGHT_ORDER

        if isElementNumber(list1[i]) and isElementNumber(list2[i]) :
            if int(list1[i]) > int(list2[i]):
                print(">False right smaller", list1[i] , list2[i])
                return NOT_RIGHT_ORDER
            elif int(list1[i]) < int(list2[i]):
                print(">True left smaller", list1[i] , list2[i])
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

correctPacketsIndices = 0
currentPaquet = 1
while True:

    line1 = data.readline().strip()
    if not line1:
        break
    pass

    line2 = data.readline().strip()
    data.readline() #empty

    packet1 = splitPacket(line1)
    packet2 = splitPacket(line2)

    print(">>>>>>")
    print(packet1)
    print(packet2)
    if listCorrectlyOrdered(packet1, packet2) == RIGHT_ODER:
        print(">",currentPaquet)
        correctPacketsIndices += currentPaquet
    currentPaquet += 1

print("R:", correctPacketsIndices)