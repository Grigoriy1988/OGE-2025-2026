a = []
for x in range(10, 100):
    if (not (x % 2 == 0)) and (not (x % 5 == 0)):
        a.append(x)
print(len(a))
