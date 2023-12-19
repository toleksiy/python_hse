# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/keszi/summa-kvadratov
n = int(input())
i = 1
qsum = 0
while i <= n:
    qsum = qsum + i ** 2
    i += 1
print(qsum)
