list_s_t = [(2, -2),(-2, 4), (4, 1), (-12, 5), (0, -7), (1, 3), (8, 2), (3, 0), (23, 1)]
count = 0
for s,t in list_s_t:
    if (s < 5) and not (t > 3):
        print("YES")
    else:
        count += 1
        print("NO")
print(f'ответ: {count}')

