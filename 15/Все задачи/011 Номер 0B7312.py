s = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a % 7 == 3:
        s += a
if s:
    print(s)
else:
    print('NO')
