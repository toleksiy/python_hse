a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
if (a * d - c * b) != 0 and a * d * c != 0:
    x = (e * d - b * f) / (a * d - c * b)
    y = (f - c * x) / d
    print(x, ' ', y)
else:
    print(0)
