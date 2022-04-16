import random

#Функция принимает данные с проверкой корректности ввода и выводит сортированный список.
def load_array():
    print('v  Введите последовательность чисел через пробел.  v')
    try:
        #костыль запятая точка для float
        a = list(map(float, input().replace(',', '.').split()))
        if len(a) < 2:
            print('Необходимо как минимум два числа. Попробуйте снова.')
            return (load_array())

        #сортируем и выводим список + число
        return sort(a, 0, len(a) - 1)
    except Exception as ex:
        print('Данные введены не верно.\n',ex, '\nЧисла следует вводить через пробел. Для нецелых допускается использовать , и . \nНапример: -968,98 .876 -22 .35 \nПопробуйте снова.')
        print(69 * '*')
        return(load_array())

#Функция ввода числа с контролем.
def load_num():
    print('v  Введите число для сравнения.  v')
    try:
        #костыль запятая точка для float
        n = float(input().replace(',', '.'))
        return n

    except Exception as ex:
        print('Данные введены не верно.\n',ex, '\nТребуется одно число. Для нецелых допускается использовать , и . \nНапример: -666,999\nПопробуйте снова.')
        print(69 * '*')
        return(load_num())

#Функция "быстрой" сортировки
def sort(array, left, right):
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
        sort(array, left, j)
    if right > i:
        sort(array, i, right)
    return(array)

array = load_array()
num = load_num()
print(array, num)
