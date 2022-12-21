import functools

def formatMonkeys(monkeys, monkey):
    try:
        return int(monkey)
    except:
        pass
    if type(monkey) is int:
        return monkey
    if monkey in monkeys and type(monkeys[monkey]) is int:
        return monkeys[monkey]
    elif monkey == "humn":
        return monkeys[monkey]
    else:
        leftOp, op, rightOp = monkeys[monkey].split(" ")
        return "({}) {} ({})".format( 
            formatMonkeys(monkeys, leftOp),
            op, 
            formatMonkeys(monkeys, rightOp)) #monkeys[rightOp] if rightOp in monkeys else rightOp))

def unrollMonkeys(monkeys, monkey, value):
    print(">",monkey, value, monkeys[monkey])
    left,op,right = monkeys[monkey].split(' ')
    try:
        left = int(left)
    except:
        right = int(right)

    if op == "+":
        if type(left) is int:
            unrollMonkeys(monkeys, right, value - left)
        else:
            unrollMonkeys(monkeys, left, value - right)
    elif op == "-":
        if type(left) is int:
            unrollMonkeys(monkeys, right, left - value)
        else:
            unrollMonkeys(monkeys, left, value + right)
    elif op == "*":
        if type(left) is int:
            unrollMonkeys(monkeys, right, value // left)
        else:
            unrollMonkeys(monkeys, left, value // right)
    elif op == "/":
        if type(left) is int:
            unrollMonkeys(monkeys, right, left // value)
        else:
            unrollMonkeys(monkeys, left, value * right)

data = open('Day21/data.txt', 'r')

monkeys = {}

while True:
    line = data.readline().strip()
    if not line:
        break
    pass
    name,call = line.split(':')
    try:
        if name == "humn":
            monkeys[name] = "XXX"
        else:
            monkeys[name] = int(call)
    except:
        monkeys[name] = call.strip()

actionsToDo = True
while actionsToDo:
    actionsToDo = False
    for monkey in monkeys.keys():

        if monkey == "humn":
            continue

        if type(monkeys[monkey]) is int:
            continue

        leftOp, op, rightOp = monkeys[monkey].split(" ")

        if type(monkeys[leftOp]) is int and type(monkeys[rightOp]) is int:
            actionsToDo = True
            if op == "+":
                monkeys[monkey] = monkeys[leftOp] + monkeys[rightOp]
            elif op == "-":
                monkeys[monkey] = monkeys[leftOp] - monkeys[rightOp]
            elif op == "*":
                monkeys[monkey] = monkeys[leftOp] * monkeys[rightOp]
            elif op == "/":
                monkeys[monkey] = monkeys[leftOp] // monkeys[rightOp]

for monkey in monkeys.keys():
        if monkey == "humn":
            continue

        if type(monkeys[monkey]) is int:
            continue

        leftOp, op, rightOp = monkeys[monkey].split(" ")
        if  type(monkeys[leftOp]) is int:
            monkeys[monkey] = "{} {} {}".format(str(monkeys[leftOp]), op, rightOp)
        if  type(monkeys[rightOp]) is int:
            monkeys[monkey] = "{} {} {}".format(leftOp, op, str(monkeys[rightOp]))

print(monkeys)
print(monkeys["root"])
unrollMonkeys(monkeys, "rpjn", 116154256834924)


