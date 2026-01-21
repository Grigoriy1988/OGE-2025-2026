s = []
while True:
    a = int(input())
    if a == 0:
        break
    if a % 7 == 5:
        s.append(a)
if s:
    print(sum(s) / len(s))
else:
    print('NO')
