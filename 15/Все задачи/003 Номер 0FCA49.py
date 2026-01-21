# вариант №1
s = 0
count = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if (a % 7) % 2 != 0:
        s += a
        count += 1
if count:
    print(s / count)
else:
    print('NO')

# вариант №2
# sr = []
# n = int(input())
# for _ in range(n):
#     a = int(input())
#     if (a % 7) % 2 != 0:
#         sr.append(a)
# if sr:
#     print(sum(sr) / len(sr))
# else:
#     print('NO')