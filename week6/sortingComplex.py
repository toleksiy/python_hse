# a = open('input.txt', 'r', encoding='utf8')
# b = open('output.txt', 'w', encoding='utf8')

numbers = list(map(int, input().split()))
# print(numbers)


def CountSort(inList):
    outList = []
    numbers1 = [0] * 101
    for now in inList:
        numbers1[now] += 1
    for i in range(len(numbers1)):
        for j in range(numbers1[i]):
            outList.append(i)
    return outList
print(*CountSort(numbers))
# a.close()
# b.close()
