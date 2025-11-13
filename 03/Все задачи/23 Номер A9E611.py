a = []
for x in range(10, 100):
    if not (x % 2 != 0) and not (x > 51):
        a.append(x)
print(len(a))
