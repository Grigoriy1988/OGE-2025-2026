n = int(input())
hour = 25
minute = 61
for _ in range(n):
    h, m = map(int, input().split())
    if hour > h:
        hour = h
        minute = m
    elif hour == h and minute > m:
        hour = h
        minute = m
print(hour, minute)
