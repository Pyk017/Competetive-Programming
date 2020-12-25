# There is a JAR full of candies for sale at a mall counter. JAR has the capacity N, that is JAR can contain maximum N candies when JAR is full.
# At any point of time. JAR can have M number of Candies where M<=N. # Candies are served to the customers. 
# JAR never remains empty as when last k candies are left. JAR is refilled with new candies in such a way that JAR gets full.
# Write a code to implement the above scenario. Display JAR at the counter with an available number of candies. 
# Input should be the number of candies one customer can order at a point of time. Update the JAR after each purchase and display JAR at Counter.

# Output should give the number of Candies sold and the updated number of Candies in JAR.

# If Input is more than candies in JAR, return: “INVALID INPUT”


# Given,

# N=10, where N is NUMBER OF CANDIES AVAILABLE

# K =< 5, where k is number of minimum candies that must be inside JAR ever.


# Example 1:(N = 10, k =< 5)

# Input Value

# 3

# Output Value

# NUMBER OF CANDIES SOLD : 3

# NUMBER OF CANDIES AVAILABLE : 7


# Example : (N=10, k<=5)

# Input Value

# 0

# Output Value
# INVALID INPUT

# NUMBER OF CANDIES LEFT : 10


def result(can):
    if can == 0 or can >= 5:
        return False
    else:
        return True


candies = int(input())
res = result(candies)
if res:
    print("NUMBER OF CANDIES SOLD : {}".format(can))
    print("NUMBER OF CANDIES AVAILABLE : {}".format(10 - can))
else:
    print("INVALID INPUT")
    print("NUMBER OF CANDIES AVAILABLE : {}".format(10))