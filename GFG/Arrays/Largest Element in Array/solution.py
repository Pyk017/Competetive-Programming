def largest( arr, n):
    return max(arr)
    

def main():
    n = int(input())
    a = [int(x) for x in input().strip().split()]
    print(largest(a, n))

        
if __name__ == "__main__":
    main()
