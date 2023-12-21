a = open('input.txt', 'r', encoding='utf8')
b = open('output.txt', 'w', encoding='utf8')
lines = a.readlines()
myList = []
threshold = 40
k = int(lines[0])
for line in lines[1:]:
    tmpEntry = line.split()

    if (int(tmpEntry[-1]) >= threshold and int(tmpEntry[-2]) >=
            threshold and int(tmpEntry[-3]) >= threshold):
        myList.append(
            int(tmpEntry[-1]) + int(tmpEntry[-2]) + int(tmpEntry[-3]))
    else:
        continue

myList.sort(reverse=True)

if len(myList) <= k or k == 0:
    print(0, file=b)
# elif myList[k - 1] == max(myList) and k != 1:
#     print(1, file=b)
else:
    for i in range(k, 0, -1):
        # print(i, myList[i])
        if myList[i] != myList[i - 1]:
            print(myList[i - 1], file=b)
            break

    else:
        print(1, file=b)


# print(myList, file=b)
a.close()
b.close()
