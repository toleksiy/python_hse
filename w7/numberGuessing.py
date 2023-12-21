n = int(input())
a = set(range(1, n))
b = set()
r = ''
while r != 'HELP':
    r = input()
    if r != 'YES' and r != 'NO' and r != 'HELP':
        b = set(map(int, r.split()))
    if r == 'YES':
        a &= b
        b = set()
    if r == 'NO':
        a -= b
        b = set()
print(*sorted(a))
