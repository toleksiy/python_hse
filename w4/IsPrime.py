def IsPrime(n):
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return 0
        i += 1
    return 1

x = int(input())
if IsPrime(x):
    print('YES')
else:
    print('NO')
