def Калькулятор(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a - 4 > 0:
        Калькулятор(a * 2, b, step - 1, k + '1')
        Калькулятор(a - 4, b, step - 1, k + '2')
    else:
        Калькулятор(a * 2, b, step - 1, k + '1')


Калькулятор(2, 24, 5)
