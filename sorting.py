import time
import random


def swap(data, i, j):
    data[i], data[j] = data[j], data[i]


def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot_value = data[int(len(data)/2)]

    i = 0
    j = len(data) - 1

    while i <= j:
        while data[i] < pivot_value:
            i += 1
        while data[j] > pivot_value:
            j -= 1
        if i <= j:
            swap(data, i, j)
            i += 1
            j -= 1

    if j > 0:
        left = quick_sort(data[0:i])
    else:
        left = data[0:i]

    if i < len(data) - 1:
        right = quick_sort(data[i:])
    else:
        right = data[i:]

    return left + right


def merge_sort(data):
    if len(data) <= 1:
        return data
    center = int(len(data)/2)
    left = merge_sort(data[:center])
    right = merge_sort(data[center:])

    j = 0
    output = []
    for i, value in enumerate(left):
        while j < len(right) and right[j] < left[i]:
            output.append(right[j])
            j += 1
        output.append(left[i])

    while j < len(right):
        output.append(right[j])
        j += 1

    return output


for n in range(0, 5):
    d = [random.randint(-10000000, 10000000) for i in range(0, 1000000)]

    c = time.clock()
    result = merge_sort(d)
    durations = time.clock() - c

    print('Merge Sort {}'.format(durations))

    c = time.clock()
    result = quick_sort(d)
    durations = time.clock() - c

    print('Quick Sort {}'.format(durations))
