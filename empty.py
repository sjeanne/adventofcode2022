import functools

data = open('data_.txt', 'r')

while True:
    line = data.readline().strip()
    if not line:
        break
    pass



# line to int
int(line)

# split line into two variables
var1, var2 = line.split(' ')

# print
print("# some log: {}".format(variable))

# one line if to assign
res = '1' if (condition) else '0'

# Load array of date 1,2,3,4,5
data = open('4/data.txt', 'r')
pickedNumbers = list(map(int,data.readline().strip().split(',')))

# Load several line of int into one array
grid = []
for i in range(5):
    grid.extend( list(map(int,data.readline().strip().split())))