def Вычислитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a - 4 > 0:
        Вычислитель(a * 4, b, step - 1, k + '1')
        Вычислитель(a - 4, b, step - 1, k + '2')
    else:
        Вычислитель(a * 4, b, step - 1, k + '1')


Вычислитель(2, 48, 5)
