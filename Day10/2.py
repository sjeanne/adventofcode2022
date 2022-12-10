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


screen = []
for x in cycles:
    cycle = len(screen)
    pixelHPos = len(screen) % 40
    if x - 1 <= pixelHPos and pixelHPos <= x + 1:
        screen.append("#")
    else:
        screen.append(("."))

for i in range(6):
    print("".join(screen[i*40:i*40+40]))
    

    