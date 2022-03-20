class Solution:    
    #Function to return a list containing the union of the two arrays.
    def mergeArrays(self,a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        a = sorted(list(set(a)))
        b = sorted(list(set(b)))
        
        combine = set(a + b)
        combine = sorted(list(combine))
        
        return combine
        
        

if __name__ == '__main__':
    n,m = map(int,input().strip().split())
    a = list(map(int,input().strip().split()))
    b = list(map(int,input().strip().split()))
    ob=Solution()
    li = ob.mergeArrays(a,b,n,m)
    for val in li:
        print(val, end = ' ')
    print()