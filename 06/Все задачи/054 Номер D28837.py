list_s_t = [(0, 2), (-1, 0), (2, 3), (4, 2), (3, 1), (-2, 7), (10, -2), (5, 4), (-7, 11)]
count = 0
for s, t in list_s_t:
    if (s < 4) and not (t < 2):
        count += 1
        print("YES")
    else:
        print("NO")
print(f'Ответ: {count}')
