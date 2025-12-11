list_s_t = [(2, -2), (5, 3), (-4, 1), (-12, 5), (5, -7), (10, 3), (-8, 12), (3, 0), (2, 3)]
count = 0
for s, t in list_s_t:
    if not ((s <= 2) and (t < 3)):
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')
