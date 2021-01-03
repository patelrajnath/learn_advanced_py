import random
from typing import List


def first(arr: List[int], low: int, high: int, x: int) -> int:
    if high >= low:
        mid = int((low + high) // 2)
        if x > arr[mid-1] and x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return first(arr, mid + 1, high, x)
        else:
            return first(arr, low, mid - 1, x)
    return -1


def last(arr: List[int], low: int, high: int, x: int) -> int:
    if high >= low:
        mid = int((low + high) // 2)
        if x < arr[mid+1] and x == arr[mid]:
            return mid
        elif x < arr[mid]:
            return last(arr, low, mid - 1, x)
        else:
            return last(arr, mid + 1, high, x)
    return -1


def binary_search(arr: List[int], low: int, high: int, x: int) -> int:
    if high >= low:
        mid = int((low + high) // 2)
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    return -1


n = 1000000
sorted_arr = sorted([random.randint(0, n) for _ in range(n)])
num = random.randint(0, n)
print(num)
i = first(sorted_arr, 0, len(sorted_arr) - 1, num)
if i == -1:
    print("Not found")
else:
    j = last(sorted_arr, 0, len(sorted_arr) - 1, num)
    print(j-i+1)
