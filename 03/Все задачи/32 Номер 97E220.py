a = []
for x in range(1,1000):
    if (x  < 8) and not (x  < 7):
        a.append(x)
print(max(a))
