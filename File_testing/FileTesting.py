import json
#import os

# два вида файла
# текстовые (.txt, .html) и бинарные (изображения, аудио, видео)

# открыть файл open()
# чтение файла read() или запись в файл write()
# закрытие файла close()

# открытие и закрытие файла
# open(file, mode)

# путь файла: абсолютный (С://) и относительный

# r (read) файл открывается для чтения
# w (write) файл открывается для записи
# a (append) файл открывается для дозаписи
# b (binary) br, bw

# myfile = open('data.txt', 'r')
# file = myfile.read()
# print(file)
# myfile.close()

# работа с файлами и исключения

# try:
#     somefile = open('hello1.txt', 'w')
#     try:
#         somefile.write('hello world')
#     except Exception as e:
#         print(e)
#     finally:
#         somefile.close()
# except Exception as ex:
#     print(ex)

# with
# with open(file, mode) as file_obj:
#     инструкции
#
# with open('hello2.txt', 'w') as somefile:
#     somefile.write('goodbye world!')

# write()

# with open('test1.txt', 'a') as file:
#     file.write('\nbye world')

# чтение файла
# 'r'
# readline() - считывает одну строку из файла
# read() - считывает все содержимое в одну строку
# readlines() - считывает все строки файла в список

# with open('17-4.txt') as f:
#     s = f.readlines()
#     a = list(map(int, s))
#     res = []
#     for i in a:
#         if str(i).count('0') >= 2 and i % 7 == 0:
#             res.append(i)
# print(max(res), len(res))

# |-3| = 3
# n % 10 == 7

# with open('17-205.txt') as f:
#     s = [int(x) for x in f]
#     res = []
#     for i in range(1, len(s)):
#         if (abs(s[i]) % 10 == 7 or abs(s[i-1]) % 10 == 7) and (s[i] + s[i-1]) % 12 == 0:
#             res.append(s[i] + s[i-1])
# print(len(res), max(res))
# try:
#     with open('24_demo.txt') as f:
#         s = f.readline()
#         m = 1
#         k = 1
#         for i in range(1, len(s)):
#             if s[i] != s[i-1]:
#                 k += 1
#                 m = max(k, m)
#             else:
#                 k = 1
#     print(m)
# except Exception as ex:
#     print('Ошибка файла', ex)

# подсчитать кол-во слов
# file = open('textpython.txt')
# data = file.read()
# words = data.split()
# print(len(words))
# file.close()

# JSON

# data = {
#     "name": "Ivan",
#     "age": 26,
#     "city": "Saratov"
# }
#
# with open('data_file.json', 'w') as f:
#     data = json.dump(data, f)
#
# with open('data_file.json', 'r') as f:
#     data1 = json.load(f)
#     print(type(data1))

# Напишите программу, которая получает от пользователя имя файла, открывает этот файл в текущем каталоге, читает его и выводит два слова: наиболее часто встречающееся из тех, что имеют размер более трех символов, и наиболее длинное слово на английском языке.

alphaeng = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
lng = 3
filename = input('Введите имя файла:')
# filename = 'file3.txt'

try:
    with open(filename, 'r', encoding='utf8') as f:
        data = f.read()
        data = data.lower()
        for i in '1234567890!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
            data = data.replace(i, '')
        words = data.split()
        # print(words)

except Exception as exf:
    print('Ошибка открытия файла', exf)

engwords = []
largewords = []
wrd1 = []
wrd2 = []
for word in words:
    tmpword = ''
    for let in word:
        for lt in alphaeng:
            if lt == let:
                tmpword += lt
    if tmpword == word:
        engwords.append(word)
        #проверяем, если смесь языков,то не добавляем
    if len(word) > lng:
        largewords.append(word)
        # Список слов > 3 букв:
#ищем повторяшки
if not len(largewords):
    print('Нет слов для вывода.')
elif len(largewords) == 1:
    print('Единственное слово: "',largewords[0], '"')
else:
    wrdtoprint = ''
    cntm = 1
    for word in largewords:
        cnt = 0
        for i in range(len(largewords)):
            if word == largewords[i]:
                cnt += 1
            if cnt == cntm and word not in wrd1:
                wrd1.append(word)
            if cnt > cntm:
                cntm = cnt
                wrd1 = [word]
    print('Наиболее часто встречающееся из тех, что имеют размер более трех символов: "', wrd1, '"')

#ищем длинное англ слово
l = 0
for word in engwords:
    if len(word) == l  and not word in wrd2:
        wrd2.append(word)
    elif len(word) > l:
        wrd2 = [word]
        l = len(word)
if wrd2:
    print('Наиболее длинное слово на английском языке:  "',wrd2, '"')
else:
    print('Слов на английском языке не найдено!')