def Калькулятор(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a <= 0 or a > 17 + 5  * 4:
        return
    Калькулятор(a * 3, b, step - 1, k + '1')
    Калькулятор(a - 4, b, step - 1, k + '2')


Калькулятор(5, 17, 5)
