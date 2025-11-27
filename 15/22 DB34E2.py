n = int(input())
min_m = 18
min_s = 30
count = 0
for _ in range(n):
    m, s = map(int, input().split())
    if m > 18 or (m == 18 and s > 30):
        continue
    else:
        count += 1
print(count)
