#Чет нечет

# num = int(input('Введите число:'))
# if num % 2 == 0:
#     print('Четное число')
# else:
#     print('Нечетное число')

#Ввод чисел и сортировка
num = int(input('Введите число:'))
data=[]
while num !=0:
    data.append(num)
    num = int(input('Введите число:'))
data.sort()
print(data)
wrd = input('Введите:')
data=[]
while wrd != '':
    if wrd not in data:
        data.append(wrd)
    wrd = input('Введите:')
for it in data:
    print(it)

# first_name = input("Введите ваше имя:")
# last_name = input("Введите вашу фамилию:")
# age = input("Введите ваш возраст:")
# city = input("Введите город проживания:")
#
# # Выводим пустую строку
# print("")
#
# # Выводим приветствие, подставляя имя и фамилию пользователя,
# # которые он ввел с клавиатуры
# print("Привет,", first_name, last_name, "!")
#
# # Выводим пустую строку
# print("")
#
# # Выводим фиксированный текст для удобства просмотра
# print("Ваш профиль:")
#
# # Выводим возраст и город, которые указал пользователь
# print("Возраст:", age, 'лет')
# print("Город:", city)

# text = input("Введите текст:")
#
# unique = list(set(text))
#
# print("Количество уникальных символов: ", len(unique))
#
#
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))
#
# L = list(map(float, input().split()))
#
# # обмениваем первое и последнее число
# # с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]
#
# # находим сумму и добавляем её в конец списка
# L.append(sum(L))
#
# print(L)


# a = input("Введите первую строку: ").split()
# b = input("Введите вторую строку: ").split()
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# print(a_set)
# print(b_set)
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# print(a_and_b)

a = 5
b = 3+2
print(id(a))
print(id(b))
print(id(b)-id(a))