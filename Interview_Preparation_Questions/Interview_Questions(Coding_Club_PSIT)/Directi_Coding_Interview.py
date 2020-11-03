# Given a array of distinct elements. The task is to check if there exits a triplet in array whose sum is zero.
# Input : 0 -1 2 -3 1
# Output : True
# or 1 2 -3 sums up to zero.


def triplet(a, n):
    a = sorted(a)
    l, r = 0, 0
    flag = False
    for i in range(n-1):
        l, r = i+1, n-1
        while l < r:
            if a[i] + a[l] + a[r] == 0:
                print("{} {} {}".format(a[i], a[l], a[r]))
                l += 1
                r -= 1
                flag = True

            elif a[i] + a[l] + a[r] < 0:
                l += 1

            else:
                r -= 1

    return flag


arr = list(map(int, input("Enter elements :- ").rstrip().split()))
res = triplet(arr ,len(arr))
if not res:
    print("No Triplet Found!")
