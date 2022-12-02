import csv

file = open("in.csv")

reader = csv.reader(file)

# Rock = A || X     worth 1
# Paper = B || Y    worth 2
# Siccors = C || Z  worth 3

score = 0

for row in reader:  
    if row[0] == 'A' and row[1] == 'X':
        score += 3 + 1
    elif row[0] == 'B' and row[1] == 'X':
        score += 0 + 1
    elif row[0] == 'C' and row[1] == 'X':
        score += 6 + 1

    elif row[0] == 'A' and row[1] == 'Y':
        score += 6 + 2
    elif row[0] == 'B' and row[1] == 'Y':
        score += 3 + 2
    elif row[0] == 'C' and row[1] == 'Y':
        score += 0 + 2

    elif row[0] == 'A' and row[1] == 'Z':
        score += 0 + 3
    elif row[0] == 'B' and row[1] == 'Z':
        score += 6 + 3
    elif row[0] == 'C' and row[1] == 'Z':
        score += 3 + 3

print(score)