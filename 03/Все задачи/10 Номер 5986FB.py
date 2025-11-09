answer = []
for x in range(1, 1000):
    if not (not ((x < 8) and (x < 21)) or (x % 2 != 0)):
        answer.append(x)
print(min(answer))
