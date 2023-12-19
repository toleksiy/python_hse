# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/cxeHQ/vozviedieniie-v-stiepien
def power1(base, exponent):
    if exponent > 1:
        return base * power1(base, exponent - 1)
    else:
        return base


a = float(input("Введите число a: "))
n = int(input("Введите число n: "))

print(f"{a} в степени {n} равно {power1(a, n)}")
