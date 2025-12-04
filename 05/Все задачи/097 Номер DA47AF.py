def Программист(a, b, step, k=''):
    if step == 0:
        print(k + f" => {a}" + '  Ошибка' if a != b else k + f" => {a}" + "   ОТВЕТ")
        return
    if a > 57:
        return
    Программист(a + 3, b, step - 1, k + '1')
    Программист(a * 3, b, step - 1, k + '2')


Программист(1, 57, 5)
