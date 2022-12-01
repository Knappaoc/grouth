import csv

file = open("Book1.csv")

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

elves.sort()
elves.reverse()

print("Highest single elf: " + str(elves[0]))
print("Highest 3 elves: " + str(sum(elves[0:3])))