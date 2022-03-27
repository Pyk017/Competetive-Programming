#User function Template for python3

def isSubset( a1, a2, n, m):
    
    for x in a2:
        if x not in a1:
            return "No"
            
    return "Yes"
            

def main():
    sz = [int(x) for x in input().strip().split()]
    n, m = sz[0], sz[1]
    a1 = [int(x) for x in input().strip().split()]
    a2 = [int(x) for x in input().strip().split()]
    
    print(isSubset( a1, a2, n, m))




if __name__ == "__main__":
    main()
