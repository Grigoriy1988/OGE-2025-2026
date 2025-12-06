def Умножитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a <= 0 or a > 18 + 5:
        return
    Умножитель(a - 1, b, step - 1, k + '1')
    Умножитель(a * 2, b, step - 1, k + '2')


Умножитель(3, 18, 5)
