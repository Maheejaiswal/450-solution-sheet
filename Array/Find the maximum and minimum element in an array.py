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
---------------------------------------------------------------------------------------
def maxi(arr):
    return max(arr)

def mini(arr):
    return min(arr)
  
arr=[1,2,3,4,5,9]
print(maxi(arr))
print(mini(arr))
---------------------------------------------------------------------------------------
def maximumElement(arr,n):
    arr.sort()
    return arr[-1]

def minimumElement(arr,n):
    arr.sort()
    return arr[0]

arr=[1,2,3,4,5,9]
print(maximumElement(arr))
print(minimumElement(arr))
