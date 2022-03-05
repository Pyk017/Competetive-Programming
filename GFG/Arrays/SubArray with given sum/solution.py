class Solution:

	def solution2(arr, n, s):
		current_sum, start = arr[0], 0

		for i in range(1, n + 1):
			while current_sum > s and start < i - 1:
				current_sum -= arr[start]
				start += 1

			if (current_sum == s):
				return [start + 1, i]

			if i < n:
				current_sum += arr[i]

		return [-1]
		

    def subArraySum(self,arr, n, s):
        sumOfArray = sum(arr)
        if (sumOfArray == s):
            return [1, n]
            
        if (sumOfArray < s):
            return [-1]
            
        if (arr[0] == s):
            return [1, 1]
            
            
        if (arr[-1] == s):
            ele = arr.index(s) + 1
            return [ele, ele]
            
            
            
        i, j, _sum = 0, 0, 0
        
        while (_sum != s and i <= j and j < n):
            
            if (_sum < s):
                _sum += arr[j]
                j += 1
                
            if (_sum > s):
                _sum -= arr[i]
                i += 1
                
        
        if (_sum == s):
            return [i + 1, j]
            
        return [-1]


        

n, s = list(map(int, input().split()))
arr = list(map(int, input().split()))
ob = Solution()
result = ob.subArraySum(arr, n, s)
for i in result:
	print(i, end=" ")



