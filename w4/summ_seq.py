def summ():
    a = int(input())
    if a == 0:
        return 0
    return a + summ()
print(summ())
