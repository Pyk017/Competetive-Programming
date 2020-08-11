# class Solution:
#     def maxSatisfaction(self, satisfaction):
        
# 		# sort largest to smallest
#         satisfaction.sort(reverse=True)
        
#         runningSum = 0
#         result = 0
#         for val in satisfaction:
#             runningSum += val
# 			# if it's no longer beneficial to serve the next dish
#             if runningSum < 0:
#                 break
#             result += runningSum
        
#         return result


def maxSatisfaction(ar):
    ar.sort(reverse=False)
    pos = len(ar)
    for i in range(len(ar)):
        if ar[i] > 0:
            pos = i
            break

    j = 0
    maxi = 0
    while j <= pos:
        k = 1
        sumi = 0
        for i in range(j, len(ar)):
            sumi += k * ar[i]
            k += 1

        if sumi > maxi:
            maxi = sumi
        j += 1

    return maxi




ar = [-1, -9, 0, 5, -7]
# s = Solution()
print(maxSatisfaction(ar))
