# N number of people participated in a coding marathon where they were asked to solve some problems. Each problem carried 1 mark and at the 
# end of the marathon. The total marks that the person achieved was calculated.
# As an organizer, you have the list of the total marks that each person achieved. You have to calculate the sum of the marks of top scores from
# the list.

# Input :
# input1 : N, the total number of participants.
# input2 : K, total score.
# input3 : An array of length N with scores of all  N participants.

# Output : 
# Return S, the sum of marks of top K scores from the list.



import heapq

def marathon(n, k, ar):
    heapq.heapify(ar)
    sumi = sum(ar)
    for i in range(n - k):
        sumi -= heapq.heappop(ar)

    return sumi

n = int(input())
k = int(input())
ar = list(map(int, input().split()))
res - marathon(n, k, ar)
print(res)
