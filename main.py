# Insertion Sort
def insertion_sort(iterable):
    for i in range(len(iterable)):
        j = i
        temp = iterable[i]
        while j > 0 and iterable[j - 1] > temp:
            iterable[j] = iterable[j - 1]
            j -= 1
        iterable[j] = temp


# Bubble Sort
def bubble_sort(iterable):
    for i in range(1, len(iterable)):
        for j in range(1, len(iterable) - i + 1):
            if iterable[j] < iterable[j - 1]:
                iterable[j], iterable[j - 1] = iterable[j - 1], iterable[j]


# Selection Sort
def selection_sort(iterable):
    for i in range(len(iterable)):
        big = 0
        for j in range(0, len(iterable) - i):
            if iterable[big] < iterable[j]:
                big = j

        iterable[j], iterable[big] = iterable[big], iterable[j]


# Merge Sort
def merge_sort(iterable):
    if len(iterable) <= 1:
        return

    mid = len(iterable) // 2
    left = iterable[:mid]
    right = iterable[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            iterable[k] = left[i]
            i += 1
        else:
            iterable[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        iterable[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        iterable[k] = right[j]
        j += 1
        k += 1


# Bucket Sort
def bucket_sort(iterable, size=100):
    if not iterable:
        return

    import math

    bucket = [[] for _ in range(size)]
    maxx = max(iterable)
    minn = min(iterable)
    ranges = maxx - minn + 1
    divide = math.ceil(ranges / size)

    for item in iterable:
        index = int((item - minn) // divide)
        bucket[index].append(item)

    for listt in bucket:
        insertion_sort(listt)

    x = 0
    for listt in bucket:
        for item in listt:
            iterable[x] = item
            x += 1


# Quick Sort
def quick_sort(iterable, recursive_limit=5_000):
    import sys

    rlimit = sys.getrecursionlimit()
    sys.setrecursionlimit(recursive_limit)
    _quick_sort(iterable)
    sys.setrecursionlimit(rlimit)


def _quick_sort(iterable):
    if len(iterable) <= 1:
        return

    import random

    pp = iterable.index(random.choice(iterable))
    pivot = iterable[pp]
    after = iterable[:pp] + iterable[pp + 1 :]
    left = [item for item in after if item <= pivot]
    right = [item for item in after if item > pivot]

    _quick_sort(left)
    _quick_sort(right)
    x = 0
    while x < len(left):
        iterable[x] = left[x]
        x += 1
    iterable[x] = pivot
    x += 1
    y = 0
    while y < len(right):
        iterable[x] = right[y]
        x += 1
        y += 1
