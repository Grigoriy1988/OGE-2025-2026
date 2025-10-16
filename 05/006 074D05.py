def Вычислитель (a, step, k = ''):
    k = k + f'{a}'
    if step == 5:
        print(k + '  Ошибка' if a != 7 else k + "   ОТВЕТ")
        return None
    if a % 2 == 0:
        Вычислитель(a * 10 + 4, step + 1, k + f'[1]->')
        Вычислитель(a // 2, step + 1, k + f'[2]->')
    else:
        Вычислитель(a * 10 + 4, step + 1, k + f'[1]->')


Вычислитель(8, 0)

