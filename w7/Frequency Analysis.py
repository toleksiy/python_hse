inFile = open('input.txt', 'r', encoding='utf8')
myDict = {}
for line in inFile:
    b = line.split()
    for i in range(len(b)):
        if (b[i]) in myDict:
            myDict[b[i]] += 1
        else:
            myDict[b[i]] = 1
myDict = sorted(myDict.items(), key=lambda item: (- item[1], item[0]))
for i in range(len(myDict)):
    print(myDict[i][0])
inFile.close()
