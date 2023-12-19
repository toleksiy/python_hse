a = int(input())  # узник замка иф: определить, пролезет ли
b = int(input())  # кирпич a*b*c в отверстие d*e
c = int(input())
d = int(input())
e = int(input())
i = 1
while i < 3:
    if a > b:
        (a, b) = (b, a)
    if b > c:
        (b, c) = (c, b)
    if d > e:
        (d, e) = (e, d)
    i += 1
if a <= d and b <= e:
    print("YES")
else:
    print("NO")
