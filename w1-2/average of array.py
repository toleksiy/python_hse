now = int(input())
qua = 1
sum = now
while now != 0:
    now = int(input())
    qua += 1
    sum += now
print(sum / (qua - 1))
