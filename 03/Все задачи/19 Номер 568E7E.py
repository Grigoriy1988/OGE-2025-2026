a = []
for x in range(1, 10000):
    if not (not ((x < 8) and (x < 21)) or (x % 2 != 0)):
        a.append(x)
print(max(a))
