def binary_search_recursive(l, s, ln, key):
    m = int((s + ln - 1) / 2)
    if s >= ln:
        return "Not Found"
    if l[m] == key:
        return m
    if l[m] < key:
        print(l[m + 1:])
        return binary_search_recursive(l, m + 1, len(l), key)
    if l[m] > key:
        print(l[0:m])
        return binary_search_recursive(l, 0, m - 1, key)


ls = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
x = binary_search_recursive(ls, 0, len(ls), int(input("Enter the search key: ")))
print("Element Found at Index : ", x, sep=' ')
