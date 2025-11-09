answer = []
for x in range(1,1000):
    if not (x < 5) and (x < 6):
        answer.append(x)
print(max(answer))