import random
from datetime import datetime

#число циклов теста
n = 10

#исходные данные
TestFile = 'dist\exmpl.txt'

with open(TestFile, encoding='utf8') as f:
    input = f.read().split()

right = len(input) - 1
print('Загружено', right+1, 'элементов для сортировки. \n')

#говно сортировка
def bad_sort(data):

    is_sort = False  # станет True, если отсортирован

    while not is_sort:  # пока не отсортирован

        random.shuffle(data)  # перемешиваем массив

        # проверяем, отсортирован ли
        is_sort = True
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                is_sort = False
                break

    return data

# Сортировка выбором
def selection_sort(data):
    for i in range(len(data)):  # проходим по всему массиву
        idx_min = i  # сохраняем индекс предположительно минимального элемента
        for j in range(i, len(data)):
            if data[j] < data[idx_min]:
                idx_min = j
        if i != idx_min:  # если индекс не совпадает с минимальным, меняем
            data[i], data[idx_min] = data[idx_min], data[i]

    return data

# Cортировка пузырьком
def buble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

# Cортировка вставками
def insert_sort(data):
    for i in range(1, len(data)):
        x = data[i]
        idx = i
        while idx > 0 and data[idx - 1] > x:
            data[idx] = data[idx - 1]
            idx -= 1
        data[idx] = x

    return data


# Сортировка слиянием
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

    return array

# Быстрая сортировка с рандомом
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
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
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

    return array

# Сортировка
def sort_sort(data):
    data.sort()
    return data

# Замеры

start_time = datetime.now()
for _ in range(n):
    selection_sort(input)
print('Сортировка выбором. Время выполнения', n, 'циклов:\n', datetime.now() - start_time)

start_time = datetime.now()
for _ in range(n):
    buble_sort(input)
print('Сортировка пузырьком. Время выполнения', n, 'циклов:\n', datetime.now() - start_time)

n = 1000
start_time = datetime.now()
for _ in range(n):
    insert_sort(input)
print('Сортировка вставками. Время выполнения', n, 'циклов:\n', datetime.now() - start_time)

start_time = datetime.now()
for _ in range(n):
    merge_sort(input)
print('Сортировка слиянием. Время выполнения', n, 'циклов:\n', datetime.now() - start_time)

start_time = datetime.now()
for _ in range(n):
    qsort(input, 0, right)
print('Сортировка быстрая. Время выполнения', n, 'циклов:\n', datetime.now() - start_time)

start_time = datetime.now()
for _ in range(n):
    qsort_random(input, 0, right)
print('Сортировка быстрая рандом. Время выполнения', n, 'циклов:\n', datetime.now() - start_time)

start_time = datetime.now()
for _ in range(n):
    sort_sort(input)
print('Сортировка Sort(). Время выполнения', n, 'циклов:\n', datetime.now() - start_time)