def selection_sort(l):
    n = len(l)

    for i in range(0, n):
        position = i
        key = l[i]
        print("Selected Pass & Key", i, l[i])
        print('\n')
        for j in range(i, n):
            if key > l[j]:
                key = l[j]
                position = j

        print("Minimum Element & Pass ", l[position], i)
        print('\n')
        m = l[i]
        l[i] = l[position]
        l[position] = m
        print(l)
    return l


ls = [2, 1, 1, 5, 4, 7, 6, 8, 10, 9]
sorted_list = selection_sort(ls)
print(sorted_list)
