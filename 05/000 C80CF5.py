def Вычислитель(a, b, step, k=''):
    # k = k + f'{a}'
    if step == 0 and a != b:
        #print(k + '  Ошибка' if a != b else k + "   ОТВЕТ")
        return None
    if step == 0 and a == b:
        print(k)
        return None
    if a % 3 == 0:
        Вычислитель(a * 10 + 1, b, step - 1, k + '1')  # + f'[1]->
        Вычислитель(a // 3, b, step - 1, k + '2')
    else:
        Вычислитель(a * 10 + 1, b, step - 1, k + '1')


Вычислитель(5, 19, 5)
