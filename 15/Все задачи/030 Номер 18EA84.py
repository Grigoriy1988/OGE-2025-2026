s = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 7 == 6:
        s.append(a)
if s:
    print(sum(s))
else:
    print('NO')
