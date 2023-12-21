a = int(input())
b = list(map(int, input().split()))
c = int(input())
delta = 10000000
val = 0
for i in range(len(b)):
    if (b[i] - c) ** 2 < delta:
        val = b[i]
        delta = (b[i] - c) ** 2
    i += 1
print(val)
