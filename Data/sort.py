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
counter = 0
for i in range(1, len(array)):
    x = array[i]
    idx = i
    while idx > 0 and array[idx-1] > x:
        counter += 1
        array[idx] = array[idx-1]
        idx -= 1
    array[idx] = x

print(array)
print(counter)

#Слияние


def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

array = [2, 3, 1, 4, 6, 5, 9, 8, 7]

# Быстрая сортировка
def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return(array)


array = [9, 3, 7]
import random
count = 0
def qsort_random(array, left = 0, right = len(array) - 1):
    global count
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            count += 1
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)
    return(array)

print(qsort_random(array))
print(count)