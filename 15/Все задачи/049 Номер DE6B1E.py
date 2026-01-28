list_3 = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 3 == 0:
        list_3.append(a)
print(len(list_3))

