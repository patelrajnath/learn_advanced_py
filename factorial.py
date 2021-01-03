import time


def factorial(num: int) -> int:
    if num == 1:
        return 1
    return num * factorial(num - 1)


n = 100
start = time.time()
print(factorial(n))
print('Recc time', time.time() - start)

start = time.time()
a = 1
m = 1
for i in range(n):
    a, m = a+1, m*a
print(m)
print('Loop time', time.time() - start)

