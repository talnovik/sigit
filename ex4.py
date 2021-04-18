

def vaild_id():
    st = input("type your id: ")
    sum = 0
    num = 0
    for n in range(0, len(st)-1, 2):
        num = int(st[n])
        while (num > 9):
            digit = num % 10
            num = int(num / 10)
            num += digit
        sum += num
    for n in range(1, len(st)-1, 2):
        num = (int(st[n]))*2
        while (num > 9):
            digit = num % 10
            num = int(num / 10)
            num += digit
        sum += num
    num = 0
    num = 10 - sum % 10

    if(num == int(st[len(st)-1])):
        return True
    else:
        return False

print(vaild_id())