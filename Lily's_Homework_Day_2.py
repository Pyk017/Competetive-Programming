<<<<<<< HEAD
def homework(a):
    dic = {a[i]: i for i in range(len(a))}
    a_sort = sorted(a)
    result = 0
    for i in range(len(a)):
        if a[i] != a_sort[i]:
            result += 1

            index = dic[a_sort[i]]
            dic[a[i]] = dic[a_sort[i]]
            a[i], a[index] = a[index], a[i]

    return result


array = list(map(int, input('Enter Array elements :- ').split()))
res = min(homework(list(array)), homework(array[::-1]))
print(res)
=======
def homework(a):
    dic = {a[i]: i for i in range(len(a))}
    a_sort = sorted(a)
    result = 0
    for i in range(len(a)):
        if a[i] != a_sort[i]:
            result += 1

            index = dic[a_sort[i]]
            dic[a[i]] = dic[a_sort[i]]
            a[i], a[index] = a[index], a[i]

    return result


array = list(map(int, input('Enter Array elements :- ').split()))
res = min(homework(list(array)), homework(array[::-1]))
print(res)
>>>>>>> competetive committed
