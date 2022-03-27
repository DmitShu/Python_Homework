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