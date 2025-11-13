a = []
for x in range(100,1000):
    if (x %10== 7) and not (x > 119):
        a.append(x)
print(len(a))
