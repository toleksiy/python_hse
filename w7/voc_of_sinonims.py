myDict = {}
myList = []
num = int(input())
for i in range(num):
    myList = input().split()
    myDict[myList[0]] = myList[1]
    myDict[myList[1]] = myList[0]
print(myDict[input()])
