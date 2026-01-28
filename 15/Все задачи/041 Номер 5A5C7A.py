message = "NO"
count = 0
n = int(input())
for _ in range(n):
    a = int(input())
    if a < 5:
        count += 1
    if a == 10:
        message = "YES"
print(count)
print(message)
