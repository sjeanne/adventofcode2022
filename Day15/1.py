import functools


def manhattanDistance(pt1,pt2):
    return abs(pt1[0]-pt2[0]) + abs(pt1[1]-pt2[1])


data = open('Day15/data.txt', 'r')
Y = 2000000
#Y = 10
caseCounted = set()
beaconSensor = set()
while True:

    line = data.readline().strip()
    if not line:
        break
    pass

    line = line.replace(',','').replace(':','').replace("x=",'').replace("y=","").split(' ')
    sensor = [int(line[2]), int(line[3])]
    beacon = [int(line[8]), int(line[9])]
    distance = manhattanDistance(sensor, beacon)

    if sensor[1] == Y:
        beaconSensor.add(sensor[0])

    if beacon[1] == Y:
        beaconSensor.add(beacon[0])

    print("Sensor:", sensor, distance)

    # for i in range(-distance, distance+1):
    #     amp = distance - abs(i)
    #     for j in range(-amp, amp+1):
    #         if (sensor[1] + j == Y): 
    #             caseCounted.add(sensor[0]+i)

    if abs(sensor[1] - Y) > distance:
        print("Sensor too far:", abs(sensor[1] - Y) - distance)
        continue

    for i in range(0, distance - abs(sensor[1] - Y) + 1):
        caseCounted.add(sensor[0] - i)
        caseCounted.add(sensor[0] + i)
    

print("Counted", len(caseCounted))
print("to sub", len(beaconSensor))