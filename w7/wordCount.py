# https://www.coursera.org/learn/python-osnovy-programmirovaniya/programming/s9LoW/kolichiestvo-slov-v-tiekstie
inFile = open("input.txt", 'r', encoding='utf8')
outFile = open("output.txt", 'w', encoding='utf8')
mySet = set()

for line in inFile:
    mySet |= set(line.split())

print(len(mySet), file=outFile)

inFile.close()
outFile.close()
