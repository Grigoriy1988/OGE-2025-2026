def Утроитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a - 1 > 0:
        Утроитель(a - 1, b, step - 1, k + '1')
        Утроитель(a * 3, b, step - 1, k + '2')
    else:
        Утроитель(a * 3, b, step - 1, k + '2')




Утроитель(4, 25, 5)