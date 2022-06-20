def collatz(number):
    if (number % 2 == 0):
        print('(even) number // 2 = ', number // 2)
        return (number // 2)
    elif(number % 2 != 0):
        print('(odd) 3 * number + 1 = ', 3 * number + 1)
        return (3 * number + 1)

    
if __name__ == '__main__':

    try:

        num = int(input('enter a number '))
        res = collatz(num)
        #print('outside while ', res)
        while(res != 1):
            res = collatz(res)
            #print('inside while', res)

    except ValueError:
        print('error')