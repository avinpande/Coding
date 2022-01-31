def shell_sort(l):
    n = len(l)
    gap = int(n / 2)
    print("Original Array ", l)
    while gap > 0:
        print(gap)
        for i in range(0, n):
            if (i + gap) < n and l[i] > l[i + gap]:
                m = l[i]
                l[i] = l[i + gap]
                l[i + gap] = m
            if (i - gap) >= 0 and l[i] < l[i - gap] and (i + gap) < n:
                m = l[i]
                l[i] = l[i - gap]
                l[i - gap] = m
        gap = int(gap / 2)
        print("Pass", l)
    return l


ls = [3, 5, 8, 8, 2, 9, 1, 0]
x = shell_sort(ls)
print("Sorted Array", x)
