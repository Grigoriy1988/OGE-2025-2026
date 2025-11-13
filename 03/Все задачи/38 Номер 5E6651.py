a = []
for x in range(1,1000):
    if not (x < 10) and (x < 11) and (x > 8):
        a.append(x)
print(max(a))
