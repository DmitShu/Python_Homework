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