# Ninja is playing with his alphabet toy. He has all the 26 lowercase alphabets. His granny wanted him to learn some maths as well.
# So, she added a cost with each of the alphabets, gave him a cost array and gave him an integer. Let us denote the integer by symbol target.
# She asks Ninja to find the greatest word(with or without meaning) under the following contrainst:

# 1. The cost array is 0 indexed and cost of using alphabet at index i is given by cost[i]. (Note: 'a' is denoted by index 0. 'b' denoted by index
#     1 and so on).
# 2. The total expenditure of characters used must be equal to target.

# You have to help Ninja to print the greatest word. If you are unable to form any word under the given contrainst, then print '0'.

# Note: if two words are given to you, then the greater of the two will be the one which comes later in the dictionary. For example:
#     'hi' is greater than 'hello'.

# Input Format:
#     The first line of input contains 26 space separated integers. The first integer denotes the cost of selecting 'a'. The second integer denotes
#     the cost of selecting 'b' and so on. The following line contains an integer, that denotes the value of the target.

# Output Format:
#     Print the greatest word under the given constraints.Print '0' if you are unable to form any word.

# Sample Input 1:
#     4 3 2 5 6 7 2 5 5 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#     9

# Sample Output 1:
#     igg

# Sample Input 2:
#     14 13 12 15 16 17 12 15 15 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
#     9

# Sample Output 2:
#     0


import string

def form(cost_array, target):
    global d
    i = len(cost_array) - 1
    res = ''
    count = 0
    while i != 0:
        if cost_array[i] + count <= target:
            res += d[cost_array[i]]
            count += cost_array[i]

        i -= 1
    return res if res != '' else '0'


cost_array = list(map(int, input().split()))
target = int(input())
d = {i: j for i, j in zip(cost_array, string.ascii_lowercase)}
res = form(cost_array, target)
print(res)
