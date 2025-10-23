# Программа перевод из произвольной системы счисления
# в десятичную
digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def f(number ,radix):
    answer = 0
    i = 0
    for dig in number[::-1].upper():
        answer += digit.index(dig) * radix**i
        i += 1
    return answer

#print(f('a1E',16))












