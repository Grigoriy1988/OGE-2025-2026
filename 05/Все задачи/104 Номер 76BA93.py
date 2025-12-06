def Удвоитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a <= 0 or a > 30 + 5 * 2:
        return
    Удвоитель(a * 3, b, step - 1, k + '1')
    Удвоитель(a - 2, b, step - 1, k + '2')


Удвоитель(2, 30, 5)
