import random as r
my_list = [1, 2, 3, "go"]
print(r.choice(my_list))

# Элемент, выбранный случайным образом

my_list = [1, 2, 3, 5, 7]

print(*my_list)


# Функция dir() возвращает список атрибутов и методов класса. Эту полезную возможность можно использовать для того чтобы получать подобные списки для различных классов при работе в интерпретаторе.


string = "A string"

print(dir(string))


# Инвертирование списка
lst = ["Fun", "is", "Programming"]

lst = lst[::-1]

print(lst) # ['Programming', 'is', 'Fun']

# Инвертирование строки

string = "Dog running on the park"

string = string[::-1]

print(string) # krap eht no gninnur goD

# Вот код функции, которая возвращает элементы последовательности, находящиеся до заданного индекса:

def cutoff(seq, index):
    if not len(seq) > index:
        return "Sorry the index is bigger than the sequence"

    return seq[:index]

long_string = "This is a long description of a blog post about Python and technology"

print(cutoff(long_string, 15))
# This is a long

print(cutoff(long_string, 70))
# Sorry the index is bigger than the sequence


