# def bubble_sort(arr):
# 	n = len(arr)
# 	count = 0
# 	for i in range(n):
# 		flag = False
# 		for j in range(n - i - 1):
			
# 			if arr[j] > arr[j + 1]:
# 				count += 1
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]
# 				flag = True


# 		if flag == False:
# 			return 'Already Sorted!'


# 	return arr


# arr = list(map(int, input().split()))
# res = bubble_sort(arr)
# print("After Sorting :- ", end=' ')
# print(*res)



# ----------------- Method 2 -----------------

# n = len(arr)

# for i in reversed(range(n)):
# 	for j in range(i):
# 		if arr[j] > arr[j + 1]:
# 			arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubbleSort(arr): 
    n = len(arr) 
   
    for i in range(n): 
        flag = False
        for j in range(n - i - 1): 

            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break
           
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
   
bubbleSort(arr) 
   
print ("Sorted array :") 
for i in range(len(arr)): 
    print ("%d" %arr[i],end=" ") 