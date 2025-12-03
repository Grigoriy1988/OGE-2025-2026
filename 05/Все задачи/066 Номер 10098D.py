def Умножитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a -1 > 0:
        Умножитель(a - 1, b, step - 1, k + '1')
        Умножитель(a * 2, b, step - 1, k + '2')
    else:
        Умножитель(a * 2, b, step - 1, k + '2')


Умножитель(3, 21, 5)
