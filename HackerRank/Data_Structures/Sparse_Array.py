n = int(input())
string = [input() for _ in range(n)]
m = int(input())
queries = [input() for _ in range(m)]
for i in queries:
    print(string.count(i))
