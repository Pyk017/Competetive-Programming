"""
Striver is the coolest boy of the college and everyone loves him too.
He was studying for his end semester exams. Meanwhile he started looking for his favourite string "JGEC" in every
sentence. He is counting the number of times the word is written in a sentence.
A sentence in his college only consists of capital english alphabets without any spaces.
Your task is to check his counting.

Input:
First line will contain T, number of testcases. Then the testcases follow.
First line of each testcase conatains an integer number N denoting the length of the sentence.
Second line of each testcase contains the string S .

Output:
For each testcase, output in a new line the answer given by Striver.

Constraints
1≤T≤10
1≤|S|≤105

Sample Input:
2
4
JGEC
15
JOLITEORJGECIAN

Sample Output:
1
1
"""
for _ in range(int(input())):
    size = int(input())
    string = input()
    print(string.count('JGEC'))
