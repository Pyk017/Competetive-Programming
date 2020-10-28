n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())

if k < 1 or j < 1 or m < 1 or p < 1:
    print("INVALID INPUT!")

else:
    if k > 0:
        atebanana = m // k
    if j > 0:
        atepea = p // j
    
    n -= (atebanana + atepea)

    print("Number of Monkeys left on the Tree: {}".format(n))
