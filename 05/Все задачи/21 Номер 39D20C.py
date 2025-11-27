def Квадратор(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a - 2 > 0:
        Квадратор(a ** 2, b, step - 1, k + '1')
        Квадратор(a - 2, b, step - 1, k + '2')
    else:
        Квадратор(a ** 2, b, step - 1, k + '1')


Квадратор(4, 142, 5)
