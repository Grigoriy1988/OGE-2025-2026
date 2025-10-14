# Вариант № 1
a = int(input())
b = int(input())
k = b - a + 1

if a % 2 == 0 and b % 2 == 0:
    count_1 = k // 2 + k % 2
else:
    count_1 = k // 2
print(count_1)
# Вариант № 2
count_2 = 0
for i in range(a, b + 1):
    if i % 2 == 0:
        count_2 += 1
print(count_2)
