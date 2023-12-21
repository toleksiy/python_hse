myList = input().split()
c = 0
for i in range(len(myList)):
    if int(myList[i]) > 0:
        c += 1
        i += 1
print(c)
