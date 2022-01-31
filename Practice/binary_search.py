def binary_search(ls, key):
    index = 0
    middle_key = int((index + len(ls)) / 2)
    if key <= ls[middle_key]:
        while index <= middle_key:
            if ls[index] == key:
                return index
            else:
                index = index + 1
    else:
        if key > ls[middle_key]:
            index = middle_key
            while index < len(ls):
                if ls[index] == key:
                    return index
                else:
                    index = index + 1
    return -1


l = [100, 200, 300, 400, 500]
x = binary_search(l, int(input()))
print(x)
