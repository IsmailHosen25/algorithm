def sortedarr(a):

    for i in range(1,len(a)):
      
      key=a[i]

      j=i-1
      while j>-1 and  a[j]>key:
         a[j+1]=a[j]
         j=j-1
      a[j+1]=key
    

arr=[1,4,2,6,3,8,2,1]
print(arr)
sortedarr(arr)
print(arr)
