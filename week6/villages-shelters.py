int(input())
villages = list(map(int, input().split()))
int(input())
bmb = list(map(int, input().split()))

vil2bmb = []
closestBmb = -1

for i in range(len(villages)):
    minDistanceToBmb = 100000
    for j in range(len(bmb)):
        if abs(villages[i] - bmb[j]) < minDistanceToBmb:
            minDistanceToBmb = abs(villages[i] - bmb[j])
            closestBmb = j
        j += 1
    vil2bmb.append(closestBmb + 1)
    i += 1

print(*vil2bmb)
