def Квадратор(a, step, k = ''):
    k = k + f'{a}'
    if step == 5:
        print(k + '  Ошибка' if a != 56 else k + "   ОТВЕТ")
        return None
    if len(str(a)) > 1:
        Квадратор(int(str(a)[1:]), step + 1, k + f'[1]->')
        Квадратор(a ** 2, step + 1, k + f'[2]->')
    else:
        Квадратор(a ** 2, step + 1, k + f'[2]->')


Квадратор(8, 0)

