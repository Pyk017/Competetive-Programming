#Rearrange Odd and Even values in Alternate Fashion in Ascending Order
# Sample Input :- 9 8 13 2 19 14
# Output :-
# Original Array is :-  2 8 9 13 14 19
# New Array is :-  2 9 8 13 14 19

def rearrange(array, even, odd):
    flag = True if array[0] % 2 == 0 else False
    i, j, k = 0, 0, 0
    while i < len(array) and j < len(even) and k < len(odd):
        if flag is True:
            array[i] = even[j]
            i += 1
            j += 1
            flag = ~flag

        else:
            array[i] = odd[k]
            i += 1
            k += 1
            flag = ~flag

    while j < len(even):
        array[i] = even[j]
        i += 1
        j += 1

    while k < len(odd):
        array[i] = odd[k]
        i += 1
        k += 1

    return array


array = sorted(list(map(int, input("Enter Array :- ").rstrip().split())))
even = list(filter(lambda x: x%2 == 0, array))
odd = list(filter(lambda x: x%2 != 0, array))
print ("Original Array is :- ",' '.join(map(str, array)))
print ("New Array is :- "," ".join(map(str, rearrange(array, even, odd))))