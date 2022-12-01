data = open('Day1/1_data.txt', 'r')

elvesCalories = []
calSum = 0
while True:
    line = data.readline()
    if not line: # get out
        break
    line = line.strip()
    if len(line) == 0: # next elf
        elvesCalories.append(calSum)
        calSum = 0
    else:
        calSum += int(line)


    
print("Elves Calories: {}".format(elvesCalories))
print("Max cal: {}".format(max(elvesCalories)))

