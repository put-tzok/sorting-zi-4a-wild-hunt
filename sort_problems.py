from random import randint
import datetime


def ns(ins):
    nss = []
    base = 5
    key = 2
    for i in range(0, ins):
        if i == 0:
            nss.append(base)
            base *= key
        else:
            nss.append(base)
            base *= key
    return nss

def fill_increasing(_len):
    arr_inc = []
    for i in range(_len):
        arr_inc.append(i)
    return arr_inc

def fill_decreasing(_len):
    arr_dec = []
    for i in range(_len, 0, -1):
        arr_dec.append(i)
    return arr_dec

def fill_vshape(_len):
    arr_vshape = []
    if _len % 2 == 0:
        for i in range(_len // 2 - 1, 0, -1):
            if i == 0:
                break
            else:
                arr_vshape.append(i)
        if _len % 2 == 0: arr_vshape.append(0)
        for i in range(0, _len // 2):
            arr_vshape.append(i)
    else:
        for i in range(_len // 2, 0, -1):
            if i == 0:
                break
            else:
                arr_vshape.append(i)
        if _len % 2 == 0: arr_vshape.append(0)
        for i in range(0, _len // 2 + 1):
            arr_vshape.append(i)
    return arr_vshape

def selection_sort(arr):
    _len = len(arr)
    for i in range(_len):
        z = i
        for j in range(i + 1, _len):
            if arr[z] > arr[j]:
                z = j
        arr[i], arr[z] = arr[z], arr[i]
    return arr


def insertion_sort(arr):
    _len = len(arr)
    for i in range(1, _len):
        z = arr[i]
        j = i - 1
        while j >= 0 and z < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = z
    return arr


def heapify(arr, i, _len):
    left = 2*i + 1
    right = 2*i + 2
    _max = i
    if left < _len and arr[left] > arr[i]:
        _max = left
    if right < _len and arr[right] > arr[_max]:
        _max = right
    if _max != i:
        arr[i], arr[_max] = arr[_max], arr[i]
        heapify(arr, _max, _len)

def build_heap(arr, _len):
    for i in range((_len-1)//2, -1,-1):
        heapify(arr, i, _len)

def heap_sort(arr):
    _len = len(arr)
    build_heap(arr, _len)
    for i in range(_len-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)
    return  arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    s = arr[0]
    left = [x for x in arr[1:] if x <= s]
    right = [x for x in arr[1:] if x > s]
    return quick_sort(left) + [s] + quick_sort(right)


def fill_random(_len):
    arr_rand = []
    for i in range(0, _len):
        arr_rand.append(randint(0, _len))
    return arr_rand

def is_random(arr):
    return arr

def is_increasing(arr):
    z = 0
    if arr[0] == min(arr): z = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]: z = 1
        elif arr[i] < arr[i - 1]:
            z = 0
            break
        elif arr[i] == arr[i - 1]:
            z = 0
            break
    if z == 1: return arr
    elif z == 0: return False


def is_decreasing(arr):
    z = 0
    if arr[0] == max(arr): z = 1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]: z = 1
        elif arr[i] > arr[i - 1]:
            z = 0
            break
        elif arr[i] == arr[i - 1]:
            z = 0
            break
    if z == 1: return arr
    elif z == 0: return False


def is_vshape(arr):
    z = 0
    j = 0
    k = -1
    _len = len(arr)
    if _len > 1:
        while arr[j] == arr[k]:
            j += 1
            k -= 1
            if j == _len - 1:
                z = 1
                break
        if _len % 2 == 0:
            for i in range(0, _len // 2 - 1):
                if arr[i] == 0:
                    z = 0
                    break
            for i in range(_len // 2 + 1, _len):
                if arr[i] == 0:
                    z = 0
                    break
        if _len % 2 != 0:
            for i in range(0, _len // 2):
                if arr[i] == 0:
                    z = 0
                    break
            for i in range(_len // 2 + 1, _len):
                if arr[i] == 0:
                    z = 0
                    break
    else:
        if arr[0] == 0: z = 1
    if z == 1:
        return arr
    elif z == 0:
        return False


def is_sorted(arr):
    z = 0
    if arr[0] == min(arr): z = 1
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]: z = 1
        elif arr[i] < arr[i - 1]:
            z = 0
            break
    if z == 1: return True
    elif z == 0: return False


fill_functions = [fill_random, fill_increasing, fill_decreasing, fill_vshape]
check_functions = [is_random, is_increasing, is_decreasing, is_vshape]
sort_functions = [selection_sort, insertion_sort, quick_sort, heap_sort]

fill_names = ["Random", "Increasing", "Decreasing", "V-Shape"]
sort_names = ["SelectionSort", "InsertionSort", "QuickSort", "HeapSort"]


def main():
    for i in range(len(sort_functions)):
        for j in range(len(check_functions)):
            for k in range(len(list(ns(10)))):
                fill = fill_functions[i](list(ns(10))[k])
                n = len(fill)
                check = check_functions[i](fill)
                current_time1 = datetime.datetime.now()
                try:
                    sort = sort_functions[i](check)
                except RecursionError:
                    print("QuickSort - maximum recursion depth exceeded")
                current_time2 = datetime.datetime.now()
                time_span = current_time2 - current_time1
                if not is_sorted(sort):
                    print("Sorting error")
                    break
                else:
                    print(sort_names[i] + " " + fill_names[j] + " " +  str(n) + " " +  str(time_span))
