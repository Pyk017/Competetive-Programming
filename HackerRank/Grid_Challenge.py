def grid_challenge(array):
    sorted_grid = [sorted(r) for r in array]
    for i in zip(*sorted_grid):
        if list(i) != sorted(list(i)):
            return 'NO'
    return 'YES'


for _ in range(int(input())):
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(input())

    result = grid_challenge(grid)
    print(result)
