def palindromecheck(num):
    pal = True
    num = str(num)
    length = len(num)
    for x in range(int(length/2)): # it repeats for half of the number's length, if it is an odd amount of numbers it doesn't matter.
        if num[x] != num [-x-1]: pal = False # if any of the pairs aren't identical, turn it off.
    num = int(num)
    if pal == False: return palindromecheck(num + 1) # if it wasn't a palindrome, go to the next number.
    else: return num # if it was a palindrome, give it back.
num = int(input("input number \n"))
temp = palindromecheck(num + 1) # if you check the same number as inputted, it will break.
print(temp)
 # largest difference between consecutive palindromic numbers.
num1 = 99999999999999999999
num2 = 99999999988999999999
print(num1 - num2)
