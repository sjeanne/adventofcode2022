import functools


def detectOverlap(elfA, elfB):
    if elfA[0] <= elfB[0] and elfB[0] <= elfA[1]:
        return True
    if elfB[0] <= elfA[0] and elfA[0] <= elfB[1]:
        return True
    if elfA[0] <= elfB[1] and elfB[1] <= elfA[1]:
        return True
    if elfB[0] <= elfA[1] and elfA[1] <= elfB[1]:
        return True
    return False

data = open('Day4/1_data.txt', 'r')

nbOverLap = 0

while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    e1, e2 = line.split(',')

    elf1 = list(map(int,e1.split('-')))
    elf2 = list(map(int,e2.split('-')))

    if detectOverlap(elf1, elf2):
        nbOverLap += 1

print("{}".format(nbOverLap))

    #print("# {}-{} {}-{}".format(elf1F, elf1L, elf2F,elf2L))