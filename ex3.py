

def ex3():
    st = input("type a string: ")
    count = 1
    output = ''
    for n in range(len(st)-1):
        if st[n] == st[n + 1]:
            count += 1
        else:
            output += st[n] + str(count)
            count = 1

    output += st[len(st)-1] + str(count)
    print(output)

ex3()