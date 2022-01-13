def palindromecheck(num):
    pal = True
    num = str(num)
    length = len(num)
    for x in range(int(length/2)):
        if num[x] != num [-x-1]: pal = False
    num = int(num)
    if pal == False: return palindromecheck(num + 1)
    else: return num
def palindromediffcheck(num):
    pal = True
    num = str(num)
    length = len(num)
    for x in range(int(length/2)):
        if num[x] != num [-x-1]: pal = False
    num = int(num)
    if pal == False: return palindromediffcheck(num - 1)
    else: return num
num = int(input("input number \n"))
temp = palindromecheck(num + 1)
print(temp)
num1 = 99999999999999999999
num2 = 99999999988999999999
print(num1 - num2)