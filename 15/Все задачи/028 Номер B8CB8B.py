# без использования функций  min и max
m = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 9 == 1 and m < a:
        m = a
if m > 0:
    print(m)
else:
    print('NO')
