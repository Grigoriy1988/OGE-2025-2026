# без использования функций  min и max
m = 30001
while True:
    a = int(input())
    if a == 0:
        break
    if a % 9 == 1 and m > a:
        m = a
if m < 30001:
    print(m)
else:
    print('NO')
