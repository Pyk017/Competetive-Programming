# The Placement Season begins in a college.  There are N number of students standing outside of an interview room in room. It is given that a person 
# who goes in first has higher chances of getting selected.
# Each Student has a number associated with them known as the Problem-solving Capability(PSC). The higher the Capability, the higher the chances of
# selection. Now, each student wants to know the number of students ahead of him/her who have more problem-solving Capability than him/her.
# Find the number for each student.

# Input :
# input1 : An integer N, which denotes the number of students present.
# input2 : An array of size N, denoting the problem-solving capability of the students.

# Output : 
# An array of size N denoting the required answer for each student.

# Example1:
# input1: 6
# input2: [4, 9, 5, 3, 2, 10]

# output1: [0, 0, 1, 3, 4, 0]


def psc_ahead(arr, n):
    count = 0
    temp = []
    temp.append(0)
    for i in range(1,n):
        for j in arr[:i]:
            if j > arr[i]:
                count += 1
        temp.append(count)
        count = 0
    return temp    

n = int(input())
arr = list(map(int, input().split()))
res = psc_ahead(arr, n)
print(*res)