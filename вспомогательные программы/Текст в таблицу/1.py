answer = open('output.txt', mode='w', encoding="utf-8")
i,e= map(str, input('Введите информационный вес одного символв в форамте "X бит" или "Y байт": ').split())
s = input('Введите текст: ')
if e == 'бит':
    i = int(i) // 8
else:
    i = int(i)
s2 = ''
s3 = ''
for letter in s[0:-1]:
    s3 += str(i) + '\t'  # str(i) + 'байт'+'\t'
    s2 += letter + '\t'
s2 += s[-1]
s3 += str(i)  # str(i) + 'байт'
answer.write(s3 + '\n')
answer.write(s2)
answer.close()
input('Результат сформирован в файл output.  \nДля завершения нажмите любую клавишу  ')