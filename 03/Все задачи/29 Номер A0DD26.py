a = []
for x in range(1,100000):
    if not (x% 2 != 0) and not (x > 14):
        a.append(x)
print(len(a))
