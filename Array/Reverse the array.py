# Write a program to reverse an array or string 
## approach 1 : slicing
'''
def reverseList(A)
  return A[::-1]
'''

## approach 2 :Recursive way
'''
def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start+1, end-1)
'''

## approach 3 : iterative way
'''
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 '''       

## reverse a string
'''
def reverseWord(s):
    rev=" "
    for i in s:
        rev=i+rev
    return rev
'''
 
  ## string reverse
'''
def reverseWord(s):
    return s[::-1]
'''
