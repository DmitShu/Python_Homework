import time
import random

#число циклов теста
n = 100

#исходные данные
TestFile = 'dist\exmpl.txt'

with open(TestFile, encoding='utf8') as f:
    input = f.read().split()

print('Загружено', len(input), 'элементов для сортировки. \n')
def chk_time(fn):
   def wrapper(*args):
       t0 = time.time()
       fn(*args)
       dt = time.time() - t0
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

    return(data)

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

    return(data)

def mean_time(fn):
    t = 0
    global n
    for _ in range(n):
        t += fn
    return t

print('Сортировка выбором. Время выполнения', n, 'циклов:\n', mean_time(selection_sort(input)))


