def merge(l, left, mid, right):
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if l[i] < l[j]:
            lm[k] = l[i]
            k = k + 1
            i = i + 1
        else:
            lm[k] = l[j]
            k = k + 1
            j = j + 1
    while i <= mid:
        lm[k] = l[i]
        i = i + 1
        k = k + 1
    while j <= right:
        lm[k] = l[j]
        j = j + 1
        k = k + 1


def mergesort(l, left, right):
    n = len(l)
    if left < right:
        mid = int((left + right) / 2)
        mergesort(l, left, mid)
        mergesort(l, mid + 1, right)
        merge(l, left, mid, right)


ls = [3, 5, 8, 2, 6, 9]
lm = [0] * len(ls)
mergesort(ls, 0, len(ls) - 1)
print("Original List", ls)
print("Sorted List", lm)
