digit = '01'
def f(number,radix):
    answer = ''
    while number > 0:
        answer = digit[number % radix] +answer
        number //= radix
    return answer


a = f(211,2)
print(f'211 в двоичной системе {a}, содержит {a.count("1")}')

