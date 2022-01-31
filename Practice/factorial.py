def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


k = fact(5)
print("Factorial", k, sep='->')
