from functools import lru_cache

# # least recently used cache
# @lru_cache(maxsize=1000)
# def fib(n):
#     # recursive method
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fib(n - 1) + fib(n - 2)


fibonaci_cach = {}


def fibb(n):
    # if we have cahced the value then return it
    if n in fibonaci_cach:
        return fibonaci_cach[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibb(n - 1) + fibb(n - 2)
    # cache the value and return it
    fibonaci_cach[n] = value
    return value


for n in range(1, 501):
    print(n, ":", fibb(n))
