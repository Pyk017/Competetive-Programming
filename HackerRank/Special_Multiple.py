from queue import Queue

def generate_pattern():
    q = Queue()
    q.put('9')
    ls = []
    i = 0
    while i < 100001:
        s1 = q.get()
        ls.append(s1)
        s2 = s1
        q.put(s1 + '0')
        q.put(s2 + '9')
        i += 1

    return ls

def solve(n, ar):
    for i in ls:
        if int(i) % n == 0:
            break

    return i

ls = generate_pattern()
n = int(input())
res = solve(n, ls)
print(res)
