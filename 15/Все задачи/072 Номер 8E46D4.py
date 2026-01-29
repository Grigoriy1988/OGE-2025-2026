list_t = []
n = int(input())
for _ in range(n):
    t = int(input())
    if t > 0:
        list_t.append(t)
print(sum(list_t) / len(list_t))
print(len(list_t))


