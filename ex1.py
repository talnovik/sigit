

def func1():
    num = '0'
    sum = 0
    while(num != "stop"):
        sum += int(num)
        num = input("enter a number, type stop to end: ")
    print("sum: " + str(sum))


def func2():
    list = input("enter numbers: ")
    arr = list.split(',')
    sum = 0
    for n in arr:
        sum += int(n)

    print("sum: " + str(sum))

func1()
func2()