# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

# Example 1:

# Input: N = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
# Example 4:

# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
# Example 5:

# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
 

# Note:

# 1 <= N <= 1000
# trust.length <= 10000
# trust[i] are all different
# trust[i][0] != trust[i][1]
# 1 <= trust[i][0], trust[i][1] <= N


def find_judge(trust, N):
    op1 = {i: 0 for i in range(1, N+1)}
    op2 = {j: 0 for j in range(1, N+1)}
    for a, b in trust:
        op1[a] += 1
        op2[b] += 1
        
    ans1 = -1
    for a, b in op1.items():
        if b == 0:
            ans1 = a
            break
        
    ans2 = -1
    for a, b in op2.items():
        if b == N - 1:
            ans2 = a
            break
                
    return ans1 if ans1 == ans2 else -1


n = int(input())
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
res = find-judge(trust, n)
print(res)
