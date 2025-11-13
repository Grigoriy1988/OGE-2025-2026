a = []
for x in range(1,1000):
    if not (not (x < 7) or (x < 6)):
        a.append(x)
print(max(a))
