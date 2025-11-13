a = []
for x in range(1,1000):
    if (not (x >= 15) and not (x < 8)) and  (x % 2 != 0):
        a.append(x)
print(max(a))
