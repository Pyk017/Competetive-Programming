from collections import Counter


def beautiful(array1, array2):
    diff = sum((Counter(array1) - Counter(array2)).values())
    return len(array1) - diff + 1 if diff else len(array1) - 1


n = int(input())
input_array1 = list(map(int, input().split()))
input_array2 = list(map(int, input().split()))
print(beautiful(input_array1, input_array2))
