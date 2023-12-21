def addIdToList(inList):
    outList = []
    for i in range(len(inList)):
        outList.append((int(inList[i]), i + 1))
    return outList

int(input())
villages = list(map(int, input().split()))
int(input())
bmb = list(map(int, input().split()))

villages1 = sorted(addIdToList(villages))
bmb1 = sorted(addIdToList(bmb))
vil2bmb = []
startBmb = 0

for i in range(len(villages1)):
    minDistanceToBmb = 1000000000
    for j in range(startBmb, len(bmb1)):
        if abs(villages1[i][0] - bmb1[j][0]) < minDistanceToBmb:
            minDistanceToBmb = abs(villages1[i][0] - bmb1[j][0])
            startBmb = j
            j += 1
        else:
            break

    vil2bmb.append((villages1[i][1], bmb1[startBmb][1]))
    i += 1
vil2bmb.sort()

for i in range(len(vil2bmb)):
    print((vil2bmb[i][1]), end=" ")
