m = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if (a % 7) % 2 != 0:
        m = max(a, m)
if m:
    print(m)
else:
    print('NO')
