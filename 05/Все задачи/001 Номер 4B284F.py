def Делитель(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(k + '  Ошибка' if a != b else k + "   ОТВЕТ")
        return
    if a % 2 == 0:
        Делитель(a // 2, b, step - 1, k + f'[1]->')
        Делитель(a + 1, b, step - 1, k + f'[2]->')
    else:
        Делитель(a + 1, b, step - 1, k + f'[2]->')


Делитель(89, 24, 5)
