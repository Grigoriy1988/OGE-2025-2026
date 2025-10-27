# Способ №1 написать программу:
def GIA(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(f'{k} Ошибка ' if a != b else f'{k} Ответ ')
        return None
    if a % 4 == 0:
        GIA(a // 4 , b, step - 1, k + f'[1]->')
        GIA(f(a), b,step - 1,  k + f'[2]->')
    else:
        GIA(f(a), b, step - 1, k + f'[2]->')

def f(x):
    s = ''
    for i in str(x):
        s+= str((int(i) + 1) % 10)
    return int(s)


GIA(128,24,5)