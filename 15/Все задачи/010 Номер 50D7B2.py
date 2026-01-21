s = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 7 == 4:
        s.append(a)
if s:
    print(sum(s) / len(s))
else:
    print('NO')
