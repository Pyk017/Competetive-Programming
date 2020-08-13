# Given schedule of trains and their stoppage time at a Railway Station, find minimum number of platforms needed.
# If Train A's departure time is x and B's arrival time is x, then we cann't accomodate Train B on the same platform as Train A.

# Input :
# First Line of input contains N denoting number of trains
# Next N line contains 2 integers, a and b, denoting the arrival time and stoppage time of train.

# Output :
# Single Integer denoting the minimum numbers of platforms needed to accomodate every train.

# Example :
# Input :
# 3
# 10 2 
# 5 10
# 13 5

# Output :
# 2

# Explaination :
# The earliest arriving train at time t=5 will arrive at platform 1. Since it will stay there till t=15, train arriving at time=10 will arrive
# at platform 2. Since it will departure at time t =12, train arriving at time t=13 will arrive at platform 2.
# Input :
# 2
# 2 4
# 6 2

# Output :
# 2


def platform(trains, n):
    count = 1
    for i in range(n - 1):
        if trains[i][0] + trains[i][1] <= trains[i + 1][0]:
            count += 1
    return count


n = int(input())
trains = []
for i in range(n):
    trains.append(tuple(map(int, input().split())))

trains.sort()
res = platform(trains, n)
print(res)
