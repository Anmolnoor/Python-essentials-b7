'''
This is a module to check weather the given number is even or odd.''
'''
def prime(num):
    '''
    This is the main function which check out the given number is even or odd.
    '''
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            return print("It is a Prime Number")
    return print("It is not a Prime Number")
n = int(input("enter the number :"))
prime(n)
