import functools

DATA_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz" #5
DATA_2 = "nppdvjthqldpwncqszvftbrmjlhg" #6
DATA_3 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" # 10
DATA_4 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #11

def findDataStream(stream):
    stream = list(stream)
    slicePos = 0
    while True:
        if len(set(stream[slicePos: slicePos+4])) == 4:
            return slicePos + 4
        slicePos += 1

data = open('Day6/1_data.txt', 'r')


line = data.readline().strip()
print(findDataStream(line))

