import functools



data = open('Day10/data.txt', 'r')
X = 1
cycles = []

while True:
    line = data.readline().strip()
    if not line:
        break
    pass


    if line == "noop":
        cycles.append(X)
        continue
    _, val = line.split(" ")
    cycles.append(X)
    cycles.append(X)
    X += int(val)

print("Res:", cycles[20-1]*20 +
    cycles[60-1]*60 +
    cycles[100-1]*100 +
    cycles[140-1]*140 +
    cycles[180-1]*180 +
    cycles[220-1]*220)

    

    