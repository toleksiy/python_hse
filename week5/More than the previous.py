a = list(map(int, input().split()))
b = a[0]
for i in a[1:]:
    if i > b:
        print(i, end=" ")
    b = i
