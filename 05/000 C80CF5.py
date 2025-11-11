def Вычислитель(a, b, step, k=''):
    k = k + f'{a}'
    if step == 0:
        print(k + '  Ошибка' if a != b else k + "   ОТВЕТ")
        return None
    if a % 3 == 0:
        Вычислитель(a * 10 + 1, b, step - 1, k + f'[1]->')
        Вычислитель(a // 3, b, step - 1, k + f'[2]->')
    else:
        Вычислитель(a * 10 + 1, b, step - 1, k + f'[1]->')


Вычислитель(5, 19, 5)
