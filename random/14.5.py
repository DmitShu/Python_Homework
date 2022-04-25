iter_obj = iter("Hello!")

print(next(iter_obj))

#Генератор.
def e():
    n = 1
    while True:
        yield (1 + 1/n)**n
        n += 1

last = 0
for a in e(): # e() - генератор
    if (a - last) < 0.00000001: # ограничение на точность
        print(a)
        break # после достижения которого - завершаем цикл
    else:
        last = a # иначе - присваиваем новое значение
L = ['THIS', 'IS', 'LOWER', 'STRING']
print(list(map(str.lower, L)))

# n=0
#
# n = int(input())
#
# print(n % 2)
def even(x):
   return x % 2 == 0

result = filter(even, [-2, -1, 0, 1, -3, 2, -3])

print(list(result))   # [-2, 0, 2]

# map + filter
some_list = [i - 10 for i in range(20)]
def pow2(x): return x**2
def positive(x): return x > 0

print(some_list)
print(list(map(pow2, filter(positive, some_list))))

# (вес, рост)
data = [
   (82, 191),
   (68, 174),
   (90, 189),
   (73, 179),
   (76, 184)
]

# Из списка в предыдущем задании найдите кортеж с минимальным индексом массы тела

print(min(data, key=lambda x: x[0] / x[1] ** 2))  # отбор по ключу