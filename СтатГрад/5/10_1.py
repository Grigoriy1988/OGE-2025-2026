digit = '01'
def f(number,radix):
    answer = ''
    while number > 0:
        answer = digit[number % radix] +answer
        number //= radix
    return answer

a = f(126,2)
print(f'126 => {a}, {a.count('1')} единиц')

