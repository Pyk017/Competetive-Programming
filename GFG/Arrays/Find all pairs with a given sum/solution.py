#User function Template for python3

class Solution:
    def allPairs(self, A, B, N, M, X):
        ans = dict()
        res = []
        for item in B:
            ans[X - item] = item
            
        # print(ans)
        
        for item in A:
            if item in ans:
                res.append([item, ans[item]])
                
                
        
    
        return sorted(res)
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        N, M, X = sz[0], sz[1], sz[2]
        A = [int(x) for x in input().strip().split()]
        B = [int(x) for x in input().strip().split()]
        ob=Solution()
        answer = ob.allPairs(A, B, N, M, X)
        sz = len(answer)
        
        if sz==0 :
            print(-1) 
        
        else: 
            
            for i in range(sz):
                if i==sz-1:
                    print(*answer[i])
                else:
                    print(*answer[i], end=', ')
        

        T -= 1


if __name__ == "__main__":
    main()




# } Driver Code Ends