massiv = []
n = int(input('Введите N = '))
for _ in range(n):
    massiv.append(float(input()))
m = massiv[0]
for i in range(1, n):
    if abs(m) > abs(massiv[i]):
        m = massiv[i]
print(f'Минимальный по модулю элемент: {m}')
print('Массив в обратном порядке:')
print('; '.join(str(a) for a in massiv[::-1]))
