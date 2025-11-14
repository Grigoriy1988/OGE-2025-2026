count = 0
for x in range(1, 1000):
    if not (x > 15) and not (x % 2 == 0):
        count += 1
print(count)
