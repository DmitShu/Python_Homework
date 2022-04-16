# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
#
# print(count)
# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1) * n
# print(fac(100))
# print(len(str(fac(100))))

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter_1 = 0

for i in range(len(array)):  # проходим по всему массиву
    idx_max = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        counter_1 += 1
        if array[j] > array[idx_max]:
            idx_max = j
    if i != idx_max:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_max] = array[idx_max], array[i]

print(array)
print(counter_1)

#Пузырек
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
counter_2 = 0

for i in range(len(array)):
    for j in range(len(array) - i - 1):
        counter_2+= 1
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(array)
print(counter_2)

#Вставки
array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print(array)