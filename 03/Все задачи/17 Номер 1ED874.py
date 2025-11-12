a = []
for x in range(1, 1000):
    if not (not ((x < 8) and (x < 21)) or (x % 2 != 0)):
        a.append(x)
print(len(a))
