list_s_t = [(13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13)]
list_A = []
for A in range(-100, 100):
    count = 0
    for s, t in list_s_t:
        if (s > A) or (t > 12):
            count += 1
            # print("YES")
        else:
            pass
            #print("NO")

    if count == 3:
        list_A.append(A)
print(f'Ответ: {max(list_A)}')
