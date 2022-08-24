print('Задача 5. Марсоход 2')
print('-' * 30)
# К роботу Валли отправили ещё одного робота Билли.
# Это его первый поход на Марс,
# поэтому он тестируется в прямоугольном помещении размером 15 на 20 метров.
# Марсоход высаживается в центре комнаты (в точке 8, 10),
# после чего управление им передаётся оператору - пользователю вашей программы.
# 
# Программа спрашивает
# в какую сторону оператор хочет направить робота:
# север (клавиша W),
# юг (клавиша S),
# запад (клавиша A)
# или восток (клавиша D).
# 
# Оператор делает выбор,
# марсоход перемещается на 1 метр в эту сторону и программа сообщает новую позицию марсохода.
# Если марсоход упёрся в стену,
# то он не должен пытаться перемещаться в сторону стены, в этом случае его позиция не меняется.
# 
# Пример:
# 
# [Программа]: Марсоход находится на позиции 6, 19, введите команду:
# [Оператор]: A
# [Программа]: Марсоход находится на позиции 5, 19, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:
# [Оператор]: W
# [Программа]: Марсоход находится на позиции 5, 20, введите команду:

width_ns  = 20      # Ширина поля
lenght_ow = 15      # Длина поля
step_ns_count = 10  # Начальная точка по ширине
step_ow_count = 8   # Начальная точка по длине

while True:
  direct = input(f'Марсоход находится на позиции, {step_ow_count},  {step_ns_count}, введите команду WSAD. Для остановки нажмите С: ')
  if direct == 'C' or direct == 'c':
      print('Игра завершена')
      print('=' * 30)
      break
  if direct == 'W' or direct == 'w':
    step_ns_count += 1
    if step_ns_count  == width_ns + 1:
      step_ns_count = width_ns
  if direct == 'S' or direct == 's':
    step_ns_count -= 1
    if step_ns_count  == - 1:
      step_ns_count = 0
  
  if direct == 'D' or direct == 'd':
    step_ow_count += 1
    if step_ow_count  == lenght_ow + 1:
      step_ow_count = lenght_ow
  if direct == 'A' or direct == 'a':
    step_ow_count -= 1
    if step_ow_count == - 1:
      step_ow_count = 0
  if step_ns_count == 0 or step_ns_count == width_ns or step_ow_count == 0 or step_ow_count == lenght_ow:
    print ('Марсоход уперся')

    '''
    Версия Никиты - преподавателя
    
    room_width, room_height = 15, 20
x, y = room_width // 2, room_height // 2
while True:
    print('Марсоход находится на позиции', x, y, ', введите команду:')
    command = input('>>>: ').lower()
    if command == "w" and y < room_height:
        y += 1
    elif command == "s" and y > 0:
        y -= 1
    elif command == "d" and x < room_width:
        x += 1
    elif command == "a" and x > 0:
        x -= 1
    '''


