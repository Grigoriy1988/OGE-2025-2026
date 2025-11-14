a = []
for x in range(1, 1000):
    if not ((x >= 23) or (x < 18)):
        a.append(x)
print(max(a))
