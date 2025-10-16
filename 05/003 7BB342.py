def Конструктор(a, step, k=''):
    k = k + f'{a}'
    if step == 5:
        print(k + '  Ошибка' if a != 9 else k + "   ОТВЕТ")
        return None
    if a % 2 == 0:
        Конструктор(a * 10 + 2, step + 1, k + f'[1]->')
        Конструктор(a // 2, step + 1, k + f'[2]->')
    else:
        Конструктор(a * 10 + 2, step + 1, k + f'[1]->')


Конструктор(14, 0)
