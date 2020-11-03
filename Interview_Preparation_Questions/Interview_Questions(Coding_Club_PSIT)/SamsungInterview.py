#  Given an array of elements and change the array in such a way that all the elements on the array are distinct.
#  if you are replacing a value, then the replacing value should be great than the previous value and after modification
# sum of the elements should be as less as possible.
# Example: arr[1, 2, 3, 4, 5, 5, 5] and the result should be [1, 2, 3, 4, 5, 6, 7] example 2 [1, 2, 5, 7, 8, 8, 7] then
# the result should be [1, 2, 5, 7, 8, 9, 10] or 1, 2, 5, 7, 8, 10, 9]
# Answer

arr = list(map(int, input().split()))
new_arr = [0]
for i in arr:
    if i > new_arr[-1]:
        new_arr.append(i)
    else:
        new_arr.append(new_arr[-1] + 1)

print(new_arr[1:])
