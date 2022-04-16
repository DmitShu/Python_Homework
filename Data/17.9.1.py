#Функция принимает данные с проверкой корректности ввода и выводит список + число.
def load_data():
    print('Введите последовательность чисел через пробел.')
    try:
        #костыль запятая точка для float
        a = list(map(float, input().replace(',', '.').split()))
        print('Введите любое число.')
        n = float(input().replace(',', '.'))
        return a, n
    except Exception as ex1:
        print('Данные введены не верно.\n',ex1, '\nПопробуйте снова.')
        print(96 * '*')
        load_data()

array, number = load_data()
print(array, number)
