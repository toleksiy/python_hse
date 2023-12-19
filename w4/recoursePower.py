n = int(input())
def power(a, n):
    if n > 0:
        power(a * a, n - 1)
    else:
        return a

print(power(a, n))
