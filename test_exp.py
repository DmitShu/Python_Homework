import time
import random

#число циклов теста
n = 666

#исходные данные
TestFile = 'dist\exmpl.txt'

with open(TestFile, encoding='utf8') as f:
    input = f.read().split()

print('Загружено', len(input), 'элементов для сортировки. \n')
def chk_time(fn):
   def wrapper(*args):
       t0 = time.time()
       fn(*args)
       dt = (time.time() - t0) / 1000
       return dt
   return wrapper

#говно сортировка
@chk_time
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
@chk_time
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
@chk_time
def buble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data

# Cортировка вставками
@chk_time
def insert_sort(data):
    for i in range(1, len(data)):
        x = data[i]
        idx = i
        while idx > 0 and data[idx - 1] > x:
            data[idx] = data[idx - 1]
            idx -= 1
        data[idx] = x

    return data

# Сортировка
@chk_time
def sort_sort(data):
    data.sort()
    return data

# Сортировка слиянием


def mean_time(fn):
    t = 0
    global n
    for _ in range(n):
        t += fn
    return t

print('Сортировка выбором. Время выполнения', n, 'циклов, c:\n', mean_time(selection_sort(input)))
print('Сортировка пузырьком. Время выполнения', n, 'циклов, c:\n', mean_time(buble_sort(input)))
print('Сортировка вставками. Время выполнения', n, 'циклов, c:\n', mean_time(insert_sort(input)))
print('Сортировка sort(). Время выполнения', n, 'циклов, c:\n', mean_time(sort_sort(input)))





