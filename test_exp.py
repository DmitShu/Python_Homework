import time
import random

#число циклов теста
n = 100
print(time.time())
#исходные данные
input = [2, 3, 1, 4, 6, 5, 9, 8, 7]

def runtime(testfn):
    print(time.time())
    global n
    a = testfn
    for _ in range(n):
        a = testfn
    print(time.time())
    return a

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

print(runtime(bad_sort(input)))
print(time.time())
