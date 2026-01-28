list_8 = []
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 8:
        list_8.append(a)
print(len(list_8))

