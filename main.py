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


# Heap Sort
def heapsort(arr):
    n = len(arr)

    heapify(arr, len(arr))

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _bubble_down(arr, 0, i)


def heapify(heap, length):
    cur = (length - 2) >> 1

    while cur >= 0:
        _bubble_down(heap, cur, length)
        cur -= 1


def heappush(heap, item):
    heap.append(item)
    _bubbleup(heap, 0, len(heap) - 1)


def heappop(heap):
    last = heap.pop()

    if not heap:
        return last

    returnitem = heap[0]
    heap[0] = last
    _bubble_down(heap, 0, len(heap))
    return returnitem


def _bubbleup(heap, start, pos):
    item = heap[pos]

    while start < pos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if parent < item:
            heap[pos] = parent
            pos = parentpos
            continue
        break

    heap[pos] = item


def _bubble_down(heap, pos, length):
    item = heap[pos]
    childpos = 2 * pos + 1

    while childpos < length:
        rightchild = 2 * pos + 2

        if rightchild < length and heap[rightchild] > heap[childpos]:
            childpos = rightchild

        if item < heap[childpos]:
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2 * pos + 1
            continue

        break

    heap[pos] = item
