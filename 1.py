import csv

file = open("Book1.csv")
file = open("test.csv")

reader = csv.reader(file)

elves = []
elf = 0
elves.append(0)

for row in reader:
    if len(row) == 0:
        elf += 1
        elves.append(0)
    else:
        elves[elf] += int(row[0])

max = 0
maxElf = 0
for elf in range(len(elves)):
    if elves[elf] > max:
        max = elves[elf]
        maxElf = elf
maxElf1 = max
elves.remove(maxElf1)

max = 0
maxElf = 0
for elf in range(len(elves)):
    if elves[elf] > max:
        max = elves[elf]
        maxElf = elf
maxElf2 = max
elves.remove(maxElf2)

max = 0
maxElf = 0
for elf in range(len(elves)):
    if elves[elf] > max:
        max = elves[elf]
        maxElf = elf
maxElf3 = max
elves.remove(maxElf3)

print(maxElf1)
print(maxElf2)
print(maxElf3)
print(maxElf1 + maxElf2 + maxElf3)