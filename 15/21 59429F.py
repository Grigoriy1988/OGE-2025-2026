n = int(input())
min_h = 25
min_m = 61
for _ in range(n):
    h,m = map(int, input().split())
    if h < min_h:
        min_h = h
        min_m = m
    elif h == min_h and m < min_m:
        min_h = h
        min_m = m
print(min_h,min_m)
