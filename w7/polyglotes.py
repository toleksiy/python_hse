# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/53SZY/polighloty
n = int(input())
allPupils = []
for i in range(n):
    m = int(input())
    mySet = set()
    for j in range(m):
        mySet.add(input())
    allPupils.append(mySet)
# print(allPupils)

allKnow = allPupils[0]
allLang = allPupils[0]

for i in range(1, len(allPupils)):
    allKnow = allKnow & allPupils[i]
    allLang = allLang | allPupils[i]

print(len(allKnow))
print(*allKnow, sep='\n')
print(len(allLang))
print(*allLang, sep='\n')
