a = []
for x in range(1,1000):
    if (x > 4) and (x < 7) and (x < 6):
        a.append(x)
print(min(a))
