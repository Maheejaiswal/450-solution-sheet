def maxMin(arr):
    max=0
    min=arr[0]
    for i in range(0, len(arr)):
        if arr[i]>max:
            max=arr[i]    
        if arr[i]<min:
            min=arr[i]
    return max, min
  
arr=[3,4,9,2]
max,min=maxMin(arr)
print(max)
print(min)
