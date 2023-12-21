inFile = open('input.txt', 'r')
myDict = dict()
for line in inFile:
    lines = line.split()
    for i in lines:
        if i not in myDict:
            myDict[i] = 0
        myDict[i] += 1
myDict = sorted(myDict.items(), key=lambda item: - item[1])
i = 0
myList = []
while i < len(myDict) and myDict[i][1] == myDict[0][1]:
    myList.append(myDict[i][0])
    i += 1
myList.sort()
print(myList[0])
