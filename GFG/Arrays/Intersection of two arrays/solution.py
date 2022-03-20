class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        setA = set(a)
        setB = set(b)
        
        setAns = setA.intersection(setB)
        
        return len(setAns)


if __name__=='__main__':
        
    n,m=[int(x) for x in input().strip().split()]
    
    a=[int(x) for x in input().strip().split()]
    b=[int(x) for x in input().strip().split()]
    ob = Solution()
    
    print(ob.NumberofElementsInIntersection(a,b,n,m))
    