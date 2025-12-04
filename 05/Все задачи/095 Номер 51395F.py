def Умножитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 36 + 5 * 10:
        return
    Умножитель(a ** 2, b, step - 1, k + '1')
    Умножитель(a - 5, b, step - 1, k + '2')


Умножитель(1, 36, 5)
