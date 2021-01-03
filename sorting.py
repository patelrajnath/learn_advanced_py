from abc import ABC
from typing import List, Optional, Callable, Any


class Sorting(object):
    def __init__(self):
        pass

    def _sort_not_implemented(self, arr: List[int]) -> Optional:
        """
        :param arr:
        :return:
        """
        raise NotImplementedError

    sort: Callable[[List[int]], None] = _sort_not_implemented

    def _call_impl(self, arr: List[int]) -> Optional:
        self.sort(arr)

    __call__: Callable[[List[int]], None] = _call_impl

    @staticmethod
    def _swap(arr: List[int], p1: int, p2: int) -> Optional:
        temp = arr[p1]
        arr[p1] = arr[p2]
        arr[p2] = temp
        return None


class BubbleSort(Sorting):
    def __init__(self):
        super(BubbleSort, self).__init__()

    def sort(self, arr: List[int]) -> Optional:
        n = len(arr)
        for i in range(n):
            no_swap = True
            for j in range(n-i-1):
                # in i-th pass, the (n-i)-th element is at the correct index
                if arr[j] > arr[j+1]:
                    self._swap(arr, j, j+1)
                    no_swap = False
            if no_swap:
                print('Pass completed', i)
                # Early stop if the list is already sorted
                break
        return None


class SelectionSort(Sorting):
    def __init__(self):
        super(SelectionSort, self).__init__()

    def sort(self, arr: List[int]) -> Optional:
        n = len(arr)
        for i in range(n):
            min_id = i
            j = i+1
            # Find the min value in remaining list and insert it at i-th location
            while j < n:
                if arr[j] < arr[min_id]:
                    min_id = j
                j += 1
            # Insert the min at i-th location
            self._swap(arr, i, min_id)


class InsertionSort(Sorting):
    def __init__(self):
        super(InsertionSort, self).__init__()

    def sort(self, arr: List[int]) -> Optional:
        n = len(arr)
        for i in range(1, n):
            j = i-1
            # Get the i-th elem as key
            key = arr[i]
            # Move the the elements of the arr one place right-side in case its gt the key
            while j >= 0 and arr[j] > key:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key


class QuickSort(Sorting):
    def __init__(self):
        super(QuickSort, self).__init__()

    def __partition(self, arr: List[int], low: int, high: int) -> Optional:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                if i != j:
                    self._swap(arr, i, j)
        if i+1 != high:
            self._swap(arr, i+1, high)
        return i + 1

    def _quick_sort(self, arr: List[int], low: int, high: int) -> Optional:
        if high > low:
            pi = self.__partition(arr, low, high)
            self._quick_sort(arr, low, pi-1)
            self._quick_sort(arr, pi+1, high)
        return None

    def sort(self, arr: List[int]) -> Optional:
        n = len(arr)
        self._quick_sort(arr, 0, n-1)
        return None


class MergeSort(Sorting):
    def __init__(self):
        super(MergeSort, self).__init__()

    def _merge(self, arr: List[int], low: int, mid: int, high: int) -> Optional:
        n1 = mid - low + 1
        n2 = high - mid

        L1 = [0] * n1
        L2 = [0] * n2

        for i in range(n1):
            L1[i] = arr[low + i]
        for j in range(n2):
            L2[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = low
        while i < n1 and j < n2:
            if L1[i] < L2[j]:
                arr[k] = L1[i]
                i += 1
            else:
                arr[k] = L2[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L1[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = L2[j]
            j += 1
            k += 1

        return None

    def _merge_sort(self, arr: List[int], low: int, high: int) -> Optional:
        if low < high:
            mid = (low + (high - 1)) // 2
            self._merge_sort(arr, low, mid)
            self._merge_sort(arr, mid+1, high)
            self._merge(arr, low, mid, high)
        return None

    def sort(self, arr: List[int]) -> Optional:
        self._merge_sort(arr, 0, len(arr)-1)


a = [400, 230, 80, 20, 40, 30, 200]
print(a)
# sort = BubbleSort()
# sort = SelectionSort()
# sort = InsertionSort()
# sort = QuickSort()
sort = MergeSort()
sort(a)
print(a)
