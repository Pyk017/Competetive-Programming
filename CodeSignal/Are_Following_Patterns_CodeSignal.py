def are_following_patterns(strings, patterns):
    for i in range(len(strings)):
        for j in range(len(strings)):
            if (strings[i] == strings[j] and patterns[i] != patterns[j]) or (strings[i] != strings[j] and patterns[i] == patterns[j]):
                return False

    return True

string = ['cat', 'dog', 'dog']
pattern = ['a', 'b', 'b']
res = are_following_patterns(string, pattern)
print(res)
