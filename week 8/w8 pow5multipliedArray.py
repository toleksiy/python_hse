from functools import reduce
print(reduce((lambda x, y: x * y), map(lambda x: x ** 5, map(int, input().split()))))
