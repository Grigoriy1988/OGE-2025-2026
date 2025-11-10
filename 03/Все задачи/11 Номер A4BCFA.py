count = 0
for x in range(10,100):
    if not (x < 88) and not(x % 2 != 0):
        count += 1
print(count)