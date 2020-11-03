# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm’s runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example:
#
# Given [5, 7, 7, 8, 8, 10]
# and target value 8,
# return [3, 4].

def search(arr, lb, ub, target):
    while (lb <= ub):
        mid = lb + (ub - lb)//2
        if arr[mid] == target:
            return mid

        elif target > arr[mid]:
            lb = mid + 1

        else:
            ub = mid - 1

    return -1

arr = list(map(int, input("Enter Element in the Array :- \n").rstrip().split()))
target = int(input("Enter Target Element :- "))
x = search(arr, 0, len(arr)-1, target)
l = []
if x == -1:
    l = [-1, -1]
else:
    y = x
    while arr[y] == arr[y - 1]:
        l.append(y - 1)
        y -= 1

    l.append(x)
    y = x
    while arr[y] == arr[y + 1]:
        l.append(y + 1)
        y += 1

print (l)
