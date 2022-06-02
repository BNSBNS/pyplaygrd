# sort accourding to frequency
def SortnAdd(arr):
    su = 0;
    arr = sorted(arr, reverse=True)
    
    if len(arr) > 4:
        for i in range(4):
            su = su + arr[i]
    else:
        for i in range(len(arr)):
            su = su + arr[i]

    return su



arr = [0,0,0,2,3,7,1]


print(SortnAdd(arr))

