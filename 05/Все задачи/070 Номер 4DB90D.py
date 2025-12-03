def Умножатор(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 84:
        return
    Умножатор(a * 3, b, step - 1, k + '1')
    Умножатор(a + 1, b, step - 1, k + '2')


Умножатор(2, 84, 5)
