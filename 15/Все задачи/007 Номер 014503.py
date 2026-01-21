s = []
while True:
    a = int(input())
    if a == 0:
        break
    if (a % 5) % 2 != 0:
        s.append(a)
if s:
    print(sum(s) / len(s))
else:
    print('NO')
