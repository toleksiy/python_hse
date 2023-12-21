p1 = "+___ "
p3 = "|__\ "
p4 = "|    "
n = int(input())
print(n * p1)
for i in range(1, n + 1):
    print("|", i, " / ", end="", sep="")
print()
print(n * p3)
print(n * p4)
