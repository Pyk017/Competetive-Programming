"""
You are given a dataset consisting of N items. Each item is a pair of a word and a boolean denoting whether the given
word is a spam word or not.

We want to use this dataset for training our latest machine learning model. Thus we want to choose some subset of this
dataset as training dataset. We want to make sure that there are no contradictions in our training set, i.e. there
shouldn't be a word included in the training set that's marked both as spam and not-spam. For example item {"fck", 1},
and item {"fck, 0"} can't be present in the training set, because first item says the word "fck" is a spam,
whereas the second item says it is not, which is a contradiction.

Your task is to select the maximum number of items in the training set.

Note that same pair of {word, bool} can appear multiple times in input. The training set can also contain the same pair
multiple times.

Input
First line will contain T, number of test cases. Then the test cases follow.
The first line of each test case contains a single integer N.
N lines follow. For each valid i, the i-th of these lines contains a string wi, followed by a space and an
integer(boolean) si, denoting the i-th item.

Output
For each test case, output an integer corresponding to the maximum number of items that can be included in the training
set in a single line.

Constraints
1≤T≤10
1≤N≤25,000
1≤|wi|≤5 for each valid i
0≤si≤1 for each valid i
w1,w2,…,wN contain only lowercase English letters

Example Input
3
3
abc 0
abc 1
efg 1
7
fck 1
fck 0
fck 1
body 0
body 0
body 0
ram 0
5
vv 1
vv 0
vv 0
vv 1
vv 1

Example Output
2
6
3
"""


for _ in range(int(input())):
    n = int(input())
    d = {}
    count = 0
    for i in range(n):
        (word, boolean) = input().split()
        if word not in d:
            if boolean == '0':
                d[word] = [1, 0]
            else:
                d[word] = [0, 1]
        elif boolean == '0':
            d[word][0] += 1
        else:
            d[word][1] += 1

    count = 0
    for k in d:
        count += max(d[k])

    print(count)
