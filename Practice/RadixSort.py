def RadixSort(ls):
    d = len(str(max(ls)))
    for i in range(0, d):
        lr = [0] * 10
        for x in ls:

            r = (int(int(x) / pow(10, i)) % 10)
            if lr[r] != 0:
                lr[r] = str(lr[r]) + "," + str(x)
            else:
                lr[r] = x
        ls[:] = [int(x) for y in lr for x in str(y).split(',') if y != 0]
    return ls


ls = [63, 250, 835, 947, 651, 28, 15, 2, 10]
print("Unsorted Array:", ls)

b = RadixSort(ls)
print("Sorted Array:", b)
