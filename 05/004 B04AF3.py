def Утроитель(a: object, step: object, k: object = ''):
    k = k + f'{a}'
    if step == 5:
        print(k + '  Ошибка' if a != 13 else k + "   ОТВЕТ")
        return None
    if a - 2 > 0:
        Утроитель(a - 2, step + 1, k + f'[1]->')
        Утроитель(a * 3, step + 1, k + f'[2]->')
    else:
        Утроитель(a * 3, step + 1, k + f'[2]->')


Утроитель(11, 0)
