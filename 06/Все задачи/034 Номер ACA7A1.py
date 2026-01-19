list_s_t = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)]
count = 0
for s, t in list_s_t:
    if (s > 10) or (t > 10):
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')
