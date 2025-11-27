# так как в задании маусимальное основание системы счисления 15,
# можно оставить только 15 символов
digit = '0123456789ABCDEF'
def f(number ,radix):
    answer = 0
    i = 0
    for dig in number[::-1].upper():
        answer += digit.index(dig) * radix**i
        i += 1
    return answer
print(f('11011011',2) + f('1110',8) - f('111',16))

#print(int('11011011',2) + int('1110',8) - int('111',15))

