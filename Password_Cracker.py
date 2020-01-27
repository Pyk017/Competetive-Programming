import sys

sys.setrecursionlimit(4000)


def crack(keys, password):
    res = []
    _crack(password, keys, res)
    print(*res) if len(res) > 0 else print("WRONG PASSWORD")


def _crack(password, keys, res):
    global memo

    if len(password) == 0:
        return True

    if password in memo:
        return False

    for key in keys:
        if password[:len(key)] == key:
            res.append(key)
            memo[password] = True

            if _crack(password[len(key):], keys, res):
                return True

            del res[-1]

    return False


n = int(input())
for _ in range(n):
    memo = {}
    input()
    crack(set(input().split(" ")), input())
