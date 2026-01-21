s = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if (a % 5) % 2 != 0:
        s += a
if s:
    print(s)
else:
    print('NO')
