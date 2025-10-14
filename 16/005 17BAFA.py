elements = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 5 == 0:
        elements.append(a)
print(sum(elements))

# Вариант без списков
# s = 0
# n = int(input())
# for _ in range(n):
#     a = int(input())
#     if a % 5 == 0:
#         s += a
# print(s)
