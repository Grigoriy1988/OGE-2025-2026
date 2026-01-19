print('Для завершения ввода и вывода ответа введи Enter')
answer = 0
while True:
    s = input(" через пробел введи знак числа, сисло и основание системы либо нажми Enter: ")
    if not s:
        break
    z, dig, radix = s.split(' ')
    answer += int(z + dig,int(radix))
print(answer)
