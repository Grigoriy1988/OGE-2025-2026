def Вычислитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 47:
        return
    Вычислитель(a * 2, b, step - 1, k + '1')
    Вычислитель(a + 3, b, step - 1, k + '2')


Вычислитель(4, 47, 5)
