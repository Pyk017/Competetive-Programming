def numberOfSoldiers(input1): 
    if (input1 == 1): 
        return 1
  
    if (input1 % 2 == 0): 
        return 2 * removeAlternate(input1 / 2) - 1
    else: 
        return 2 * removeAlternate(((input1 - 1) / 2)) + 1
  
# Driver code 

n = int(input())
print(n - removeAlternate(n))
print(removeAlternate(n) - (n - 1)) 