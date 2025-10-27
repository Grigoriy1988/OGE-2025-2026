# Способ №1 написать программу:
def GIA(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(f'{k} Ошибка ' if a != b else f'{k} Ответ ')
        return None
    if a % 2 == 0:
        GIA(a // 2, b, step - 1, k + f'[1]->')
        GIA(a - 1, b,step - 1,  k + f'[2]->')
    else:
        GIA(a - 1, b,step - 1,  k + f'[2]->')




GIA(28, 10, 5)
