import time

N = 100


def decorator_time(fn):
   def wrapper():
       t0 = time.time()
       result = fn()
       dt = time.time() - t0
       return dt
   return wrapper


def pow_2():
   return 10000000 ** 2


def in_build_pow():
   return pow(10000000, 2)


pow_2 = decorator_time(pow_2)
in_build_pow = decorator_time(in_build_pow)

mean_pow_2 = 0
mean_in_build_pow = 0
for _ in range(N):
   mean_pow_2 += pow_2()
   mean_in_build_pow += in_build_pow()

print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.2f}")
print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / 100:.2f}")
#
# def my_decorator(fn):
#    def wrapper():
#        fn()
#    return wrapper  # возвращается задекорированная функция, которая заменяет исходную
#
# # выведем незадекорированную функцию
# def my_function():
#    pass
# print(my_function)  # <function my_function at 0x7f938401ba60>
#
# # выведем задекорированную функцию
# @my_decorator
# def my_function():
#    pass
# print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>
#
# def my_decorator(fn):
#     print("Этот код будет выведен один раз в момент декорирования функции")
#     def wrapper(*args, **kwargs):
#         print('Этот код будет выполняться перед каждым вызовом функции')
#         result = fn(*args, **kwargs)
#         print('Этот код будет выполняться после каждого вызова функции')
#         return result
#     return wrapper

# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
# print(say_word('123'))
# print(say_word('123'))
# print(say_word('123'))


# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper
#
# @cache
# def f(n):
#    return n * 123456789
# print(f(1))
# print(f(2))
# print(f(3))
# print(f(4))