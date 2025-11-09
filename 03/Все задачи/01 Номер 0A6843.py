answer = []
for x in range(100,1000):
    if x % 10 == 3 and not(x < 230):
        answer.append(x)
print(min(answer))