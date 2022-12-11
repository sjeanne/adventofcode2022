import functools

def computeWorryLevel(currentWorry, operation):
    newWorryLevel = 0
    if operation["value"] == "old" and operation["op"] == "*":
        newWorryLevel = currentWorry * currentWorry
    else:
        if operation["op"] == "*":
            newWorryLevel = currentWorry * int(operation["value"])
        else:
            newWorryLevel = currentWorry + int(operation["value"])
    return newWorryLevel // 3

data = open('Day11/data.txt', 'r')
monkeys = []

while True:
    monkey = {}

    line = data.readline().strip()
    if not line:
        break
    pass

    #Monkey number
    #Starting items
    _, listItems = data.readline().strip().split(":")
    monkey["items"] = list(map(int, listItems.strip().split(",")))
    monkey["activities"] = 0
    #Operation
    _,_,_,_,op,val = data.readline().strip().split(" ")
    monkey["operation"] = {"op":op, "value":val}
    #Test
    monkey["divide"] = int(data.readline().strip().split(" ")[3])
    #If
    monkey["TrueTo"] = int(data.readline().strip().split(" ")[5])
    #else
    monkey["FalseTo"] = int(data.readline().strip().split(" ")[5])
    # empty line separator
    data.readline().strip()

    monkeys.append((monkey))


# READY TO RUMBLE !!!

NB_ROUNDS = 20
currentRound = 0
while NB_ROUNDS > currentRound:
    for monkey in monkeys:
        monkey["activities"] += len(monkey["items"])
        for item in monkey["items"]:
            newItemWorry = computeWorryLevel(item, monkey["operation"])
            if newItemWorry % monkey["divide"] == 0:
                monkeys[monkey["TrueTo"]]["items"].append(newItemWorry)
            else:
                monkeys[monkey["FalseTo"]]["items"].append(newItemWorry)
        monkey["items"] = []
    currentRound += 1
    print("** ROUND ",  currentRound)
    print(*monkeys)

activities = list(map(lambda monkey: monkey["activities"], monkeys))
activities.sort(reverse=True)
print(activities[0], activities[1], activities[0] * activities[1])



    

    