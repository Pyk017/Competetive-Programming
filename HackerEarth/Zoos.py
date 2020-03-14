# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/
string = input()
print("Yes") if string.startswith('z') and string.endswith("o") and 2*string.count('z') == string.count("o") else \
    print('No')
