print('Первый способ')
count = 0
a = int(input())
b = int(input())
for i in range(a, b + 1):
    if i % 2 == 0:
        count += 1
print(count)


print('Второй способ')
a = int(input())
b = int(input())
k = (b // 2) - ((a - 1) // 2)
print(k)

