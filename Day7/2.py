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
            #folders[path] += int(size)
            subpathes = []
            for subpath in pwd:
                subpathes.append((subpath))
                subpathcommplete = "/".join(subpathes)

                if not( subpathcommplete in folders):
                    folders[subpathcommplete] = 0

                folders[subpathcommplete] += int(size)
            folders[""] += int(size)



print( folders)

totalSpaceUsed = folders[""]
currentFreeSpace = 70000000 - totalSpaceUsed
spaceToFree = 30000000 - currentFreeSpace

pathsToDelete = []

for folder in folders:
    folderSize = folders[folder]
    if folderSize >= spaceToFree:
        pathsToDelete.append((folderSize))

print(pathsToDelete)

print(min(pathsToDelete))

