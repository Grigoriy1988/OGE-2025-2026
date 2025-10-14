# elements = []
# n = int(input())
# for _ in range(n):
#     a = int(input())
#     if (a % 5) % 2 !=0:
#         elements.append(a)
# if elements:
#     print(sum(elements)/len(elements))
# else:
#     print('NO')

# Вариант без списков
s = 0
count = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if (a % 5) % 2 != 0:
        s += a
        count += 1
if count:
    print(s / count)
else:
    print('NO')
