# Способ №1 написать программу:
def GIA(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(f'{k} Ошибка ' if a != b else f'{k} Ответ ')
        return None
    if a >= 10:
        GIA(a // 10, b, step - 1, k + f'[1]->')
        GIA(a*2, b,step - 1,  k + f'[2]->')
    else:
        GIA(a*2, b,step - 1,  k + f'[2]->')


# for x in range(25,36):
#     GIA(x, 10, 5)
#     print()
GIA(29, 40, 5)
