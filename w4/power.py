a = float(input())
n = int(input())


def power(a, n):
    if n == 1:
        return a
    elif n == 0:
        return 1
    return a * power(a, n - 1)


print(power(a, n))
