n = int(input())
count = 0
f = False
for _ in range(n):
    a = int(input())
    if a == 10:
        f = True
    if a < 5:
        count += 1
print(count)
print("Yes" if f else "No")
