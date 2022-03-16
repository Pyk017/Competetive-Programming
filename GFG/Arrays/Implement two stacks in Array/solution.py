'''
Input Format:

First line contains an integer Q denoting the number of queries . 
A Query Q is of 4 Types
(i)    1 1 x    (a query of this type means  pushing 'x' into the stack 1)
(ii)   1 2      (a query of this type means to pop element from stack1  and print the poped element)
(iii)  2 1 x  (a query of this type means pushing 'x' into the stack 2)
(iv)  2 2     (a query of this type means to pop element from stack2 and print the poped element)
The second line contains Q queries seperated by space.

Example:

6
1 1 2 1 1 3 2 1 4 1 2 2 2 2 2
'''

#Function to push an integer into the stack1.
def push1(a,x):
    global top1
    top1 += 1
    a[top1] = x

    
#Function to push an integer into the stack2.
def push2(a,x):
    global top2
    top2 -= 1
    a[top2] = x

    
#Function to remove an element from top of the stack1.    
def pop1(a):
    global top1
    if top1 == -1:
        return -1
    
    top1 -= 1
    return a[top1 + 1]

    
#Function to remove an element from top of the stack2.    
def pop2(a):
    global top2
    if top2 > 100:
        return -1
        
    top2 += 1
    return a[top2 - 1]
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

top2=101
top1=-1

if __name__ == '__main__':    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    a = [-1 for i in range(101)] # array to be used for the 2 stacks.
    i=0 # curr index
    while i<len(arr):
        if arr[i] == 1:
            if arr[i+1] == 1:
                push1(a,arr[i+2])
                i+=1
            else:
                print(pop1(a),end=" ")
            i+=1
        else:
            if arr[i+1] == 1:
                push2(a,arr[i+2])
                i+=1
            else:
               print(pop2(a),end=" ")
            i+=1
        i+=1
    top2=101
    top1=-1
    print(' ')
