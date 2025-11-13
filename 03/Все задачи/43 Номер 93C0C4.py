a = []
for x in range(1,1000):
    if (x < 5) or not (x > 3):
        a.append(x)
print(max(a))
