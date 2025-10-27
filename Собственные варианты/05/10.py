# Способ №1 написать программу:
def GIA(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(f'{k} Ошибка ' if a != b else f'{k} Ответ ')
        return None
    if a // 100 > 0:
        GIA(a * 2, b, step - 1, k + f'[1]->')
        GIA(int(str(a)[2:]), b,step - 1,  k + f'[2]->')
    else:
        GIA(a * 2, b,step - 1,  k + f'[1]->')



for i in range(125,130):
    GIA(i, 10, 5)
    print()
GIA(129, 24, 5)