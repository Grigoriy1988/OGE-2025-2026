import csv

with open("pets.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    n = input()
    s = set()
    for row in reader:
        s.add(row[n])
    for i in sorted(s):
        print(i)
