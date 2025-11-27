def Раздвоитель(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a % 2 == 0:
        Раздвоитель(a -1 , b, step - 1, k + '1')
        Раздвоитель(a // 2, b, step - 1, k + '2')
    else:
        Раздвоитель(a - 1, b, step - 1, k + '1')


Раздвоитель(21, 3, 5)
