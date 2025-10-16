def Квадратор(a, step, k = ''):
    k = k + f'{a}'
    if step == 5:
        print(k + '  Ошибка' if a != 6 else k + "   ОТВЕТ")
        return None
    if a // 10 > 0:
        Квадратор(a ** 2, step + 1, k + f'[1]->')
        Квадратор(a // 10, step + 1, k + f'[2]->')
    else:
        Квадратор(a ** 2, step + 1, k + f'[1]->')


Квадратор(3, 0)

