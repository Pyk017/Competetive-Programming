# Problem Statement :- Given an array, rotate the array to the right by k steps, where k is non-negative.  
def rotate(array, key):
    for i in range(key):
        temp = array[-1]
        for j in range(len(array)-1 ,  0, -1):
            array[j] = array[j-1]

        array[0] = temp
        temp = 0

    return array

array = list(map(int, input("Enter elements in the Array :- ").rstrip().split()))
key = int(input("Enter key :- "))
print ("New Array is :- ",rotate(array, key))