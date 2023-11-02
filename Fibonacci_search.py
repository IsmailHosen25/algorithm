def fibonacci_search(arr,x):
    l = len(arr)
    elim = -1
    fn_2 = 0    #Two finbonacci numbers before fn
    fn_1 = 1    #One finonacci numbers before fn
    fn = fn_1+fn_2
    while fn<l:
        fn_2 = fn_1
        fn_1 = fn 
        fn = fn_1+fn_2
    while fn>1:
        #Note: Searching after the 'elim' factor
        curr = min(elim+fn_2,l-1)  #To ensure index is within range
        if arr[curr] == x:
            return curr     #Returning the found index
        elif arr[curr] > x:   #Then element is first 1/3rd
            fn = fn_2
            fn_1 = fn_1 - fn_2
            fn_2 = fn_2 - fn_1   #Moving two down
        else:   #arr[curr] < x
            fn = fn_1
            fn_1 = fn_2
            fn_2 = fn - fn_1   #Moving 1 down
            elim = curr   #eliminating upto curr from 0 index
    return -1
arr = [ 2, 3, 4, 10, 40 ]
x = 4
result = fibonacci_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")