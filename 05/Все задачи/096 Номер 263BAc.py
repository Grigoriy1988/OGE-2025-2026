def Программист(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a <= 0 or a > 44 + 5 * 1:
        return
    Программист(a - 1, b, step - 1, k + '1')
    Программист(a * 4, b, step - 1, k + '2')


Программист(1, 44, 5)
