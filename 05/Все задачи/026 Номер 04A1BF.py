def Квадратор(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    Квадратор(a**2, b, step - 1, k + '1')
    Квадратор(a+2, b, step - 1, k + '2')



Квадратор(1, 85, 5)