def Удвоитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a <= 0 or a > 66 + 5 * 3:
        return
    Удвоитель(a - 3, b, step - 1, k + '1')
    Удвоитель(a * 5, b, step - 1, k + '2')


Удвоитель(3, 66, 5)
