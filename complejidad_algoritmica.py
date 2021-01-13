import time
import sys


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    
    return n * factorial_r(n - 1)

if __name__ == '__main__':
    n = 10
    sys.setrecursionlimit(10000000)

    for i in range(5):
        exp = n ** (i + 1);
        print("n = ", exp)
        comienzo = time.time()
        factorial(exp)
        final = time.time()
        print(final - comienzo)

        comienzo = time.time()
        factorial_r(exp)
        final = time.time()
        print(final - comienzo)
