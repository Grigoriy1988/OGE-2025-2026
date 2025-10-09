count = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 7 == 1:
        count += 1
if count:
    print(count)
else:
    print('NO')
