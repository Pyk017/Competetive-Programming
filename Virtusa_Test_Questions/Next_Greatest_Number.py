def nextGreater(input1, input2):
    a = list(input1)
    for i in reversed(range(len(a) - 1)):
        if a[i] < a[i + 1]:
            break
    else: 
        return False

    j = next(j for j in reversed(range(i + 1, len(a))) if a[i] < a[j])

    a[i], a[j] = a[j], a[i]

    a[i + 1:] = reversed(a[i + 1:])
    return ''.join(a)


n = int(input())
num = input()
print(nextGreater(num, n))
