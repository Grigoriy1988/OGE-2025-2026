with open("a.txt", "r", encoding='utf-8') as file:
    s = file.read()
print(s)
answer = open('output.txt', mode='w', encoding="utf-8")
s2 = ''
for i in s[0:-1]:
    s2 += i + '\t'
s2 += s[-1]
answer.write(s2)
answer.close()
print(s2)
