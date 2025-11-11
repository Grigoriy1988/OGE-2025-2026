count = 0
for x in range(1, 101):
    if not ((x >= 33) or (x < 19)) and (x % 2 == 0):
        count += 1
print(count)