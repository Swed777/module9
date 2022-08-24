print('Задача 6. Спецшифр')
print('-' * 30)
# Два сотрудника спецслужб переписываются необычным шифром.
# Каждую букву они шифруют в виде строки,
# внутри которой есть длинная последовательность букв “s”, 
# а длина самой длинной - это и есть номер буквы алфавита, которую хотят отправить.
# 
# Напишите программу,
# которая получает на вход строку,
# подсчитывает в ней самую длинную последовательность подряд идущих букв “s” и выводит ответ на экран.
# 
# Пример:
# Введите строку: ssbbbsssbc
# Самая длинная последовательность: 3

long_sym = input('Введите зашифрованное слово: ')
count = 0
max = 0

for symbol in long_sym:
  if symbol == 's':
    count += 1
  elif max < count:
       max = count
       count = 0
if count > max:
    max = count
  
print('--> Самая длинная последовательность: ', max)

print('=' * 30)


"""
long_s = input('Введите зашифрованное слово: ')
count_prev = 0
count_curr = 0

for symbol in long_s:
  if symbol == 's':
    count_curr += 1
  else:
    if count_curr > count_prev:
      max = count_curr
       count_prev = count_curr
       count_curr = 0
  count_prev = count_curr   
  
print('--> Самая длинная последовательность: ', count_prev, count_curr)
"""