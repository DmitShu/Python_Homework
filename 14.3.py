def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
#for num in fib():
#   print(num)
def genn(num = 1, stp = 1):
    cnt = num
    while True:
        yield cnt
        cnt Далее программа работает по следующему алгоритму:

Преобразование введённой последовательности в список

Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)

Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.+= stp
nump = genn()
for i in range(10):
    print(next(nump))

# Создайте генератор цикла, то есть в функцию на входе будет передаваться массив, например, [1, 2, 3], генератор будет вечно работать возвращая 1 2 3 1 2 3… и так далее.
#
# Решение
def repeat_list(list_):
   list_values = list_.copy()
   while True:
       value = list_values.pop(0)
       list_values.append(value)
       yield value

# for i in repeat_list([1, 2, 3]):
#    print(i)

# str_ = "my tst"
# str_iter = iter(str_)
# print(type(str_))  # строка
# print(type(str_iter))  # итератор строки
# # Получим первый элемент строки
# print(next(str_iter))  # m
#
# # Получим ещё несколько элементов последовательности
# print(next(str_iter))  # y
# print(next(str_iter))  #
# print(next(str_iter))  # t
# print(next(str_iter))  # s
# print(next(str_iter))  # t
# print(next(str_iter))