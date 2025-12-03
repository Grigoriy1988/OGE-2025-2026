def Вычислитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 39:
        return
    Вычислитель(a * 5, b, step - 1, k + '1')
    Вычислитель(a + 2, b, step - 1, k + '2')


Вычислитель(1, 39, 5)
