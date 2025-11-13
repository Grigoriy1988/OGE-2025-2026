a = []
for x in range(1,100000):
    if (not (x >= 15) and not (x < 8)) and (x % 2 != 0):
        a.append(x)
print(len(a))
