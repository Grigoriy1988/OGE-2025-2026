a = []
for x in range(1,1000):
    if not (x % 2 != 0) and not (x > 12):
        a.append(x)
print(len(a))
