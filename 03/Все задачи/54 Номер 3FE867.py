a = []
for x in range(1, 1000):
    if not ((x >= 53) or (x < 29)):
        a.append(x)
print(len(a))
