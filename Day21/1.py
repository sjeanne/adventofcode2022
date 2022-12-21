import functools


data = open('Day21/data.txt', 'r')

monkeys = {}

while True:
    line = data.readline().strip()
    if not line:
        break
    pass
    name,call = line.split(':')
    try:
        monkeys[name] = int(call)
    except:
        monkeys[name] = call.strip()

print(monkeys)

while not (type(monkeys["root"]) is int):
    for monkey in monkeys.keys():
        if type(monkeys[monkey]) is int:
            continue
        leftOp, op, rightOp = monkeys[monkey].split(" ")

        if type(monkeys[leftOp]) is int and type(monkeys[rightOp]) is int:
            if op == "+":
                monkeys[monkey] = monkeys[leftOp] + monkeys[rightOp]
            elif op == "-":
                monkeys[monkey] = monkeys[leftOp] - monkeys[rightOp]
            elif op == "*":
                monkeys[monkey] = monkeys[leftOp] * monkeys[rightOp]
            elif op == "/":
                monkeys[monkey] = monkeys[leftOp] // monkeys[rightOp]
    print(monkeys)
print(monkeys["root"])