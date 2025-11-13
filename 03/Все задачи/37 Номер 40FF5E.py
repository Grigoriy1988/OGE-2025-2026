count = 0
for x in range(10, 100):
    if not (x % 2 == 0) and not (x > 67):
        count += 1
print(count)
