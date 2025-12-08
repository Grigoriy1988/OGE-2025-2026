list_s_t = [(13, 2), (11, 12), (-12, 12), (2, -2), (-10, -10), (6, -5), (2, 8), (9, 10), (1, 13)]
list_A = []
for A in range(-100, 100):
    count = 0
    for s, t in list_s_t:
        if(s > A) or (t > 12):
            pass
            # print("YES")
        else:
            count += 1
            #print("NO")

    if count == 5:
        list_A.append(A)
print(f'Ответ: {len(list_A)}')
