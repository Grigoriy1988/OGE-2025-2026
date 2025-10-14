elements = []
n = int(input())
for _ in range(n):
    a = int(input())
    if (a % 9) == 1:
        elements.append(a)
if elements:
    print(min(elements))
else:
    print('NO')
