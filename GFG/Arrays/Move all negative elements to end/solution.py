#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        pos = [x for x in arr if x >= 0]
        neg = [y for y in arr if y < 0]
        
        i, j = 0, 0
        
        while i < len(pos):
            arr[i] = pos[i]
            i += 1
            
        while j < len(neg):
            arr[i] = neg[j]
            j += 1
            i += 1
        
        

def main():
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    ob=Solution()
    ob.segregateElements(a, n)
    print(*a)


if __name__ == "__main__":
    main()
