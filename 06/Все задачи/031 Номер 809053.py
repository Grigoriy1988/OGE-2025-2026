list_s_t = [(-5, -2), (5, 3), (-14, 3), (-12, 5), (5, -7), (10, 3), (-4, 3), (3, 0), (-4, 9)]
count = 0
for s, t in list_s_t:
    if not ((s < -4) and (t >= 3)):
        print("YES")
    else:
        count += 1
        print("NO")
print(f'Ответ: {count}')
