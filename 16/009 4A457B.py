# Решение на основе списков
# numbers = []
# n = int(input())
# for _ in range(n):
#     a = int(input())
#     if a % 10 ==2:
#         numbers.append(a)
# print(min(numbers))
m = 30002
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 2 and a < m:
        m = a
print(m)
