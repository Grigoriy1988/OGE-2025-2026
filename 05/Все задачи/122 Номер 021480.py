def Вычислитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 90:
        return
    Вычислитель(a + 3, b, step - 1, k + '1')
    Вычислитель(a * 3, b, step - 1, k + '2')


Вычислитель(1, 90, 5)
