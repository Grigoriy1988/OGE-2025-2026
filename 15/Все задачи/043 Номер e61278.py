count = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a % 10 == 9:
        count += 1
print(count)
