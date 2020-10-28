def machine(weight):
        
    if weight == 7000:
        return "OVERLOADED"
    
    if weight >= 1 and weight <= 2000:
        return "Time Estimated: 25 minutes"
    
    if weight >=2001 and weight <=4000:
        return "Time Estimated: 35 minutes"

    if weight >= 4001:
        return "Time Estimated: 45 minutes"

    return "INVALID INPUT"


weight = int(input())
res =  machine(weight)
print(res)