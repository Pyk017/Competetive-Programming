'''
Given a string and a special character separated with comma. Find the total number of substring in which special character did not present.
Input : abcd,b
Ouput : 4
Explanation : a ab abc abcd    (All Substrings)
                b bc bcd
                    c cd
                        d
        
        a c cd d are those 4 substring that does not contain b in it. 
'''


def calculate(n):
    return (n * (n + 1)) // 2

word, k = input().split(',')
pos = word.index(k) + 1
left = pos - 1
right = len(word) - pos
result = calculate(left) + calculate(right)
print(result)