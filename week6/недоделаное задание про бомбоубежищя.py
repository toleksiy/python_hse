""" def addIdToList(inList):
    outList = []
    for i in range(len(inList)):
        outList.append((int(inList[i]), i + 1))
    return outList

def sortIndex(inList):
    return inList[][0] """

int(input())
villages = list(map(int, input().split()))
int(input())
bmb = list(map(int, input().split()))


"""villages = [50, 100, 30, 40]
bmb = [80, 10, 60]
villages1 = addIdToList(villages)
bmb1 = addIdToList(bmb)"""


vil2bmb = []
closestBmb = -1

for i in range(len(villages)):
    minDistanceToBmb = 100000
    for j in range(len(bmb)):
        if abs(villages[i] - bmb[j]) < minDistanceToBmb:
            minDistanceToBmb = abs(villages[i] - bmb[j])
            closestBmb = j
        j =+ 1
    vil2bmb.append(closestBmb + 1)
    i += 1 

print(*vil2bmb)

# outList = [(50, 1), (20, 2), (30, 3)]