def findmaximum(input1, input2, input3):
    d = list(zip(input1, input2))
    total = 0
    for i, j in d:
        if j == 'P':
            total += i
        else:
            total -= i

    return total * 100
    

arr = list(map(int, input().split()))
string = input()
electro = int(input())
print(findmaximum(arr, string, electro))
