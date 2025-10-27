# Способ №1 написать программу:
def GIA(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(f'{k} Ошибка ' if a != b else f'{k} Ответ ')
        return None
    if a % 3 == 0:
        GIA(a // 3, b, step - 1, k + f'[1]->')
        GIA(int('2'+str(a)), b,step - 1,  k + f'[2]->')
    else:
        GIA(int('2'+str(a)), b,step - 1,  k + f'[2]->')


for x in range(3,7):
    GIA(x, 10, 5)
    print()
GIA(4, 76, 5)
