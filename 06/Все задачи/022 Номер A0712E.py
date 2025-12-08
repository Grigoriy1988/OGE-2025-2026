list_s_t = [(2, -2), (5, 3), (14, 1), (-12, 5), (5, -7), (10, 3), (8, 2), (3, 0), (23, 9)]
count = 0
for s, t in list_s_t:
    if not ((s >= 5) and (t < 3)):
        print("YES")
    else:
        count += 1
        print("NO")
print(f'Ответ: {count}')
