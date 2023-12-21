string = input()
pos = string.find('f')
if pos >= 0:
    string2 = string[pos + 1:]
    pos2 = string2.find('f')
    if pos2 >= 0:
        print(pos + pos2 + 1)
    else:
        print(-1)
else:
    print(-2)
