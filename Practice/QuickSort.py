def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <= j and A[j] > pivot:
            j = j - 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j


def quicksort(A, low, high):
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi - 1)
        quicksort(A, pi + 1, high)


import sys

sys.setrecursionlimit(1000)
A = []
for x in range(0, 100):
    A.append(x)
print('Original Array:', A)
quicksort(A, 0, len(A) - 1)
print('Sorted Array:', A)
