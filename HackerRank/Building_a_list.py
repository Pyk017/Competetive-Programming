def subsequence(string):
    if len(string) == 1:
        return [string]
    subs = subsequence(string[1:])
    print(subs)
    return [string[0]+i for i in subs] + subs + [string[0]]


def solve(s):
    return sorted(subsequence(s))


t = int(input())
for _ in range(t):
    n = int(input())
    input_string = input()
    print(solve(input_string))
