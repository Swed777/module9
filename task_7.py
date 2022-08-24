print('Задача 7. Великий и могучий')
print('-' * 30)
# Паоло изучает русский язык: занимается по учебникам, читает книги, слушает музыку.
# Особенно Паоло понравилась книга “Преступление и наказание”.
# И ему стало интересно,
# какое можно найти самое длинное слово в этой книге, чтобы потом сравнить его с аналогом на своём языке.
# 
# Напишите программу,
# которая получает на вход текст и находит длину самого длинного слова в нём.
# Слова в тексте разделяются одним пробелом.
# 
# Пример:
# Введите текст: Меня зовут Петр
# Длина самого длинного слова: 5

max = 0
count = 0
string = input('Введите фразу для анализа (разделитель слов - 1 пробел): ')

for letter in string:
  if letter != ' ':
    count += 1
  elif max < count:
    max = count
    count = 0
if max < count:
   max = count
print('Длина самого длинного слова:', max)


print('=' * 30)