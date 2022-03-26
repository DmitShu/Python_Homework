def fib():
    a, b = 0, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b
#for num in fib():
#   print(num)
def genn(num = 1, stp = 1):
    cnt = num
    while True:
        yield cnt
        cnt = cnt + stp

