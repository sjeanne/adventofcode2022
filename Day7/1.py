import functools

data = open('Day7/data.txt', 'r')

pwd = []
folders = {}
while True:
    line = data.readline().strip()
    if not line:
        break
    pass

    if line.find("$ cd") == 0:
        _,_,path = line.split(' ')
        if path == "..":
            pwd.pop()
        elif path == "/":
            pwd = []
        else:
            pwd.append(path)
        pass
    elif line.find("$ ls") == 0:
        pass
    else:
        size,file = line.split(" ")
        if size == "dir":
            pass
        else:
            path = "/".join(pwd)
            if not( path in folders):
                folders[path] = 0
            folders[path] += int(size)


print( folders)

totalSmallFolders = 0
for folder in folders:
    folderSize = folders[folder]
    for subFolders in folders:
        if subFolders.find(folder) == 0 and subFolders != folder:
            folderSize += folders[subFolders]
    if folderSize <= 100000:
        totalSmallFolders += folderSize

print(totalSmallFolders)

