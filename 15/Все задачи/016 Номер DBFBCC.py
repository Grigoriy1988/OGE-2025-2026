count = 0
while True:
    a = int(input())
    if a == 0:
        break
    if a % 7 == 1:
        count += 1
if count:
    print(count)
else:
    print('NO')
