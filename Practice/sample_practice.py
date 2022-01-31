ls = [20, 30, 30, 20, 10]
ls[:] = [(x / 10) for x in ls]
for x in range(0, 5):
    print(x)


for x in ls:
    if x == 20 :
        list(x).append(10)
print(len(ls))
