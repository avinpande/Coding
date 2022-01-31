ls = [100, 20, 10, 2, 5, 19, 120]


def linear_search(key, index=0):
    while index < len(ls):
        if ls[index] == key:
            return index
        else:
            index = index + 1
    return -1


x = linear_search(int(input("Enter the search key :")), 0)
print("Element found at index: ", x)
