#Високосный или нет
#x = int(input("Введите год:"))
#print(x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))
# N = int(input("Введите число:"))
# print('3' and '7' in str(N))

# Создайте скрипт, который будет в input() принимать строки, их необходимо будет конвертировать в числа, добавьте try-except, чтобы строки могли быть сконвертированы в числа.
#
# В случае удачного выполнения скрипта пусть выведется: «Вы ввели правильное число».
#
# В конце скрипта обязательно должна быть надпись «Выход из программы».
#
# ПРИМЕЧАНИЕ: Для отлова ошибок используйте try-except, а также блоки finally и else.
#
# Примеры входов и выходов:

# try:
#     i = int(input("Ввведите число:"))
# except ValueError as e:
#     print("Вы ввели неправильное число (Ошибка:)",e)
# else:
#     print("Вы ввели неправильное число ",i)
# finally:
#     print("Выход из программы")

#Запишите условие, которое является истинным, когда только одно из чисел А, В и С меньше 45. Иногда проще записать все условия и не пытаться упростить их.
# A = int(input('Ввведите А'))
# B = int(input('Ввведите B'))
# C = int(input('Ввведите C'))
# if ((A < 45) and (B>=45) and (C>=45)) or\
#    ((B < 45) and (A >= 45) and (C >= 45)) or\
#    ((C < 45) and (B >= 45) and (A >= 45)):
#     print("условие выполнено")
# else:
#     print("условие не выполнено")
#Запишите логическое выражение, которое определяет, что число А не принадлежит интервалу от -10 до -1 или интервалу от 2 до 15.
A = int(input('Ввведите А '))
if not ((-10 <= A <= -1) or (2 <= A <= 15)):
    print("не принадлежит")
else:
    print("принадлежит")