#Функции
# объявили функцию для подсчета количества символов в тексте
def char_frequency():
   text = """
   У лукоморья дуб зелёный;
   Златая цепь на дубе том:
   И днём и ночью кот учёный
   Всё ходит по цепи кругом;
   Идёт направо -- песнь заводит,
   Налево -- сказку говорит.
   Там чудеса: там леший бродит,
   Русалка на ветвях сидит;
   Там на неведомых дорожках
   Следы невиданных зверей;
   Избушка там на курьих ножках
   Стоит без окон, без дверей;
   Там лес и дол видений полны;
   Там о заре прихлынут волны
   На брег песчаный и пустой,
   И тридцать витязей прекрасных
   Чредой из вод выходят ясных,
   И с ними дядька их морской;
   Там королевич мимоходом
   Пленяет грозного царя;
   Там в облаках перед народом
   Через леса, через моря
   Колдун несёт богатыря;
   В темнице там царевна тужит,
   А бурый волк ей верно служит;
   Там ступа с Бабою Ягой
   Идёт, бредёт сама собой,
   Там царь Кащей над златом чахнет;
   Там русский дух... там Русью пахнет!
   И там я был, и мёд я пил;
   У моря видел дуб зелёный;
   Под ним сидел, и кот учёный
   Свои мне сказки говорил.
   """

   text = text.lower()
   text = text.replace(" ", "")
   text = text.replace("\n", "")

   count = {}  # для подсчета символов и их количества
   for char in text:
       if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
           count[char] += 1
       else:
           count[char] = 1

   for char, cnt in count.items():
       print(f"Символ {char} встречается {cnt} раз")

...

# вызвали функцию в любом месте программы
#char_frequency()

def add2and2():
    print (2+2)
#add2and2()

# функция, которая возводит любое число в степень n
def pow_func(base, n=2):
   print(base ** n)

#pow_func(3)  # 9
#pow_func(5, 3)  # 125

def get_multipliers(a):
   count = 0
   for n in range(1, a + 1):
       if a % n == 0:
           count += 1

   return count

#print(get_multipliers(5))  # 2
#print(get_multipliers(4))  # 3
#Проверка полиндром.
def check_palindrome(str_):
   str_ = str_.lower()
   str_ = str_.replace(" ", "")

   if str_ == str_[::-1]:
       return True
   else:
       return False

#check_palindrome("test")  # False
#check_palindrome("Кит на море не романтик")  # True
def adder(*nums):
    sum_ = 1
    for n in nums:
        sum_ *= n

    return sum_


print(adder())  # 0
print(adder(1))  # 1
print(adder(1, 2))  # 3
print(adder(1, 2, 3))  # 6

def rec_sum(n):
   if n == 1:  # терминальный случай
       return 1
   return n + rec_sum(n - 1)  # рекурсивный вызов

def sum_digit(n):
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)

sum_digit(123)  # 6