# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/5tQ5s/shokoladka
a1 = int(input())  # коробки: определить, влезет ли кор a1b2c3 в a2b2c2?
b1 = int(input())  # d в коробку a2b2c2
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
i = 1
while i < 3:
    if a1 > b1:
        (a1, b1) = (b1, a1)
    if b1 > c1:
        (b1, c1) = (c1, b1)
    if a2 > b2:
        (a2, b2) = (b2, a2)
    if b2 > c2:
        (b2, c2) = (c2, b2)
    i += 1
if a1 == a2 and b1 == b2 and c1 == c2:
    print("Boxes are equal")
if a1 > a2 and b1 > b2 and c1 > c2:
    print("The first box is smaller than the second one")
if a1 < a2 and b1 < b2 and c1 < c2:
    print("The first box is smaller than the second one1")
else:
    print("Boxes are incomparable")
