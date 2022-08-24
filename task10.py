print('Задача 10. Метод бутерброда')
print('-' * 30)
# Секретное агентство «Super-Secret-no» решило
# для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке:
# первая буква получает номер 1,
# последняя буква - номер 2,
# вторая – номер 3,
# предпоследняя – номер 4, потом третья … и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.
# 
# Например, слово «sandwich» зашифруется в «shacnidw».
# 
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им.
# 
# Пример:
# Введите зашифрованное сообщение: shacnidw
# Расшифрованное сообщение: sandwich
#          1   3   5   7   8   6   4   2
# Слово: | s | a | n | d | w | i | c | h |
#
# Шифр:  | s | h | a | c | n | i | d | w |


word = (input('Введите зашифрованное слово: '))

for count, value in enumerate(word, start = 1):
 # print(count, value)
  if count % 2 != 0:
    print(value, end='')

for count, value in enumerate(reversed(word)):
  if count % 2 == 0:
    print(value, end='')


print('\n')
print('=' * 30)


'''
Версия преподавателя Никиты

word = input('Введите зашифрованное слово: ')
sum_1, sum_2  = '', ''
count = 0
for letter in word:
    count += 1
    if count % 2 != 0:
        sum_1 += letter
    else:
        sum_2 = letter + sum_2
print('Расшифрованное слово: ', sum_1 + sum_2)

'''
'''
Версия с сайта https://www.cyberforum.ru/python-tasks/thread2879341.html

a, tmp, res, definitely_not_len = input(), '', '', 0
 
for i in a:
    definitely_not_len += 1
 
for i in range(definitely_not_len):
    if not i % 2:
        res += a[i]
    else:
        tmp += a[i]
 
print(res + tmp[::-1])
'''