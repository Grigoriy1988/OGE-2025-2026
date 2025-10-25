# Поляков Задача № 8355
count = 0
answer = []
for x in range(10, 100):
    f1 = x > 67 and x % 2 == 0
    f2 = x > 67 and (x // 10) % 2 == 0
    f3 = x % 2 == 0 and (x // 10) % 2 == 0

    if (f1 and not f2 and not f3) or (not f1 and f2 and not f3) or (not f1 and not f2 and f3):
        answer.append(x)
        count += 1
print(count)
print(answer)
