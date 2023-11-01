def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
arr=[2,1,6,1,45678,8,2,8,4,6,9,4]
print(arr)
insertion_sort(arr)
print(arr)