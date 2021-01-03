import time


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


n = 35
# start = time.time()
# for i in range(n):
#     print(i, fib(i))
# print("Time rec", time.time()-start)

start = time.time()
a = 0
b = 1
for i in range(n):
    print(a)
    a, b = b, a + b
print("Time loop", time.time()-start)

