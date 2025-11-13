a = []
for x in range(1,1000):
    if not (x > 19) and not (x % 2 == 0):
        a.append(x)
print(len(a))
