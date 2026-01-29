list_t = []
n = int(input())
for _ in range(n):
    list_t.append(int(input()))
min_t = min(list_t)
print(min_t)
print("YES" if min_t < -15 else "NO")


