import functools

DATA_1 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" #19
DATA_2 = "bvwbjplbgvbhsrlpgdmjqwftvncz" #23
DATA_3 = "nppdvjthqldpwncqszvftbrmjlhg" # 23
DATA_4 = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg" #29
DATA_5 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw" #26

def findDataStream(stream):
    stream = list(stream)
    slicePos = 0
    while True:
        if len(set(stream[slicePos: slicePos+14])) == 14:
            return slicePos + 14
        slicePos += 1

data = open('Day6/1_data.txt', 'r')


line = data.readline().strip()
print(findDataStream(line))

