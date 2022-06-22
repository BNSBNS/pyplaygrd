spam = ['apples', 'bananas','tofu','cats']

def newfunc(ar):

    ar.insert(-1,'and')
    
    for i in range(len(ar)):
        
        # so i will end 1 short of length, as length starts from 1, and i from 0
        if(i+1 == len(ar)):
            print(ar[i])

        else:
            print(ar[i], ', ', end='')

newfunc(spam)