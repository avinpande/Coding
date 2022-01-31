def insertion_sort(l):
    n = len(l)
    for i in range(0, n):
        for j in range(0, n - 1):
            if l[j + 1] < l[j]:
                m = l[j]
                l[j] = l[j + 1]
                l[j + 1] = m

        print("Pass", i, l)
    return l


ls = [3, 5, 8, 9, 6, 2]
x = insertion_sort(ls)
print("Sorted List ", x)
