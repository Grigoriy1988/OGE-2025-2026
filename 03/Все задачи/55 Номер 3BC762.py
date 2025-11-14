a = []
for x in range(1, 1000):
    if not ((x == 2) or not (x < 3)):
        a.append(x)
print(min(a))
