count = 0
for x in range(99, 9, -1):
    if not(not (x % 2 == 0) and not (x % 13 == 0)):
        count += 1
print(count)