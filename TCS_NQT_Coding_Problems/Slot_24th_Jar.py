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