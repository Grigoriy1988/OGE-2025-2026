def Делитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a % 2 == 0:
        Делитель(a // 2, b, step - 1, k + '1')
        Делитель(a - 1, b, step - 1, k + '2')
    else:
        Делитель(a - 1, b, step - 1, k + '2')


Делитель(27, 5, 5)
