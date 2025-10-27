# Способ №1 написать программу:
def GIA(a, b, step, k=''):
    k = k + f'{a}'
    if step == 6:
        print(f'{k} Ошибка ' if a != b else f'{k} Ответ ')
        return None
    if a % 10 != 0 and a % (a%10) == 0:
        GIA(a + 2, b, step + 1, k + f'[1]->')
        GIA(a // (a%10), b,step + 1,  k + f'[2]->')
    else:
        GIA(a + 2, b, step + 1, k + f'[1]->')

#
# for x in range(14,25):
#     GIA(x, 10, 1)
#     print()
GIA(23, 5, 1)
