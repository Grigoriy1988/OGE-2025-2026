list_s_t = [(2, -2), (5, 3), (14, 1), (-12, 5), (5, 7), (10, 3), (8, 2), (3, 0), (-4, 9)]
count = 0
for s, t in list_s_t:
    if not (s > -4) or (t < 3):
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')
