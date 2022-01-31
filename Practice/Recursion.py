def sum_demo(n):
    if n == 1:
        return 1
    else:
        return sum_demo(n - 1) + n


k = sum_demo(500)
print(k)
