def Квадратор(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 26:
        return
    Квадратор(a ** 2, b, step - 1, k + '1')
    Квадратор(a + 1, b, step - 1, k + '2')


Квадратор(1, 26, 5)
