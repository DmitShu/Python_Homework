import random

#Функция принимает данные с проверкой корректности ввода и выводит список + число.
def load_data():
    print('Введите последовательность чисел через пробел.')
    try:
        #костыль запятая точка для float
        a = list(map(float, input().replace(',', '.').split()))
        print('Введите любое число.')
        n = float(input().replace(',', '.'))
        #сортируем и выводим список + число
        return sort(a, 0, len(a) - 1), n

    except Exception as ex1:
        print('Данные введены не верно.\n',ex1, '\nПопробуйте снова.')
        print(96 * '*')
        load_data()

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

array, number = load_data()
print(array, number)
