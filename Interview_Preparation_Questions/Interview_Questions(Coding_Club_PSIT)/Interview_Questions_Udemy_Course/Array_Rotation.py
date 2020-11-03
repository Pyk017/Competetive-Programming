# Given two array we have to return True if one array is the rotation of another array else return False. 
# Input: [1,2,3,4,5,6,7]
#         [4,5,6,7,1,2,3]
# Output : True

def is_rotated(a, b):
    diff, temp = 0, 0
    if len(a) != len(b):
        return False
    for i, j in enumerate(a):
        try:
            diff = abs(i - b.index(j))
            if temp == 0 and diff == 0:
                return False
            else:
                if temp == 0:
                    temp = diff
                else:
                    if diff != temp:
                        return False
        except:
            return False

    return True


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(is_rotated(A, B))
