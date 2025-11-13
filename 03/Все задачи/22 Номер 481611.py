a = []
for x in range(1, 100):
    if not (x % 2 != 0) and not (x > 18):
        a.append(x)
print(len(a))
