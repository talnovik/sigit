def map(func, list):
    arr = []
    for x in list:
        arr.append(func(x))
    return arr


def multi(x):
    return x*2


print(map(multi, [1, 2, 3]))