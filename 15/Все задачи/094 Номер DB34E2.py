n = int(input())
count = 0
for _ in range(n):
    h, m = map(int, input().split())
    if h < 18 or (h == 18 and m <= 30):
        count += 1
print(count)
