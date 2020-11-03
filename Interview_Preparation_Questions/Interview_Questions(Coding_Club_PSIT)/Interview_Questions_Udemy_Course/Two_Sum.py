# Given a list of nuumbers and a number of k, return whether any two number from the list adds up to k.
# Input : list = [10, 15, 3, 7], k = 17
# Output : True

def two_sum(ar, k):
    di = {}
    diff = 0
    for i in ar:
        diff = k - i
        if diff in di:
            return True
        else:
            di[i] = i

    return False

arr = list(map(int, input().split()))
K = int(input())
print(two_sum(arr, K))    