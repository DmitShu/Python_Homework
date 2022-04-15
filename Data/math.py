import math

n = 10000

print((n ** 2) / (n * math.log2(n)))

def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)
