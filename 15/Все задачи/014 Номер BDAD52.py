# без списков, классический способ решения
count = 0
s = 0
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 7) % 2 != 0:
        count += 1
        s += a
if count:
    print(s / count)
else:
    print('NO')
