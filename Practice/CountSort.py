def countSort(A):
    bin_size = max(A)
    b = [0] * (bin_size + 1)
    for x in A:
        b[x] = b[x] + 1
    i = 0
    j = 0
    while j < bin_size + 1:
        if b[j] > 0:
            A[i] = j
            i = i + 1
            b[j] = b[j] - 1
        else:
            j = j + 1


A = [2, 3, 3, 0, 0, 8, 9, 7]
countSort(A)
print('Sorted Array', A)
