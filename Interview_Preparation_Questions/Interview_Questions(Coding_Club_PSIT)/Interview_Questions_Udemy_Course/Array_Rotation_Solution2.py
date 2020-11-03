# Given two array we have to return True if one array is the rotation of another array else return False. 
# Input: [1,2,3,4,5,6,7]
#         [4,5,6,7,1,2,3]
# Output : True

def is_rotated(a, b):
    if len(a) != len(b):
        return False

    key = a[0]
    key_i = -1
    for i in range(len(b)):
        if b[i] == key:
            key_i = i
            break
    if key_i == -1:
        return False

    for i in range(len(a)):
        j = (key_i + i) % len(a)
            if a[i] != b[j]:
            return False

    return True


A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(is_rotated(A, B))
