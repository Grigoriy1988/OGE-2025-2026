import csv

bird = {}
while True:
    s = input()
    if not s:
        break
    s = s.split(": ")
    bird[s[0]] = [s[1]]

while True:
    s = input()
    if not s:
        break
    s = s.split(": ")
    bird[s[0]].append(s[1])

while True:
    s = input()
    if not s:
        break
    s = s.split(": ")
    bird[s[0]].append(s[1])
bird = dict(sorted(bird.items()))

with open("birds.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['no', 'bird', 'song', 'time', 'place'])
    for i, v in enumerate(bird, start=1):
        line = [str(i), v]
        line.extend(bird[v])
        writer.writerow(line)
