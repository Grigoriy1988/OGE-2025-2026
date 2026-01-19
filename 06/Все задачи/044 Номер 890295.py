list_s_t = [(1, 2), (11, 2), (1, 12), (11, 12), (-11, -12), (-11, 12), (-12, 11), (10, 10), (10, 5)]
list_A = []
for A in range(-100, 100):
    count = 0
    for s, t in list_s_t:
        if (s > 10) or (t > A):
            pass
            # print("YES")
        else:
            count += 1
            #print("NO")

    if count == 4:
        list_A.append(A)
print(f'Ответ: {list_A}')
