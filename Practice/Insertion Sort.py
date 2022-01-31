def insertion_sort(l):
    n = len(l)
    for i in range(0, n):
        position = i
        for j in range(i - 1, -1, -1):
            if l[position] < l[j]:
                m = l[j]
                l[j] = l[position]
                l[position] = m
                position = j

        print("Pass", i, l)
    return l


ls = [1, 2, 3, 4, 5, 6, 7]
x = insertion_sort(ls)
print("Sorted List ", x)
