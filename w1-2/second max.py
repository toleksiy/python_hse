now = 1
nowMax = now
max2 = 0
while now != 0:
    now = int(input())
    if now > nowMax:
        max2 = nowMax
        nowMax = now
    elif now > max2:
        max2 = now
print(max2)
