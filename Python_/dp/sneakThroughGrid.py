grid = [
    [".", ".", "<", "."],
    ["X", "A", ".", "X"],
    [".", "<", ".", "."],
    ["X", ".", "X", "."],
]


def isPossible(grid):
    ROW, COL = len(grid), len(grid[0])
    seen = set()
    nonTraverse = set()
    start = [0, 0]

    def travel(r, c):
        if r < 0 or c < 0 or r >= ROW or c >= COL or (r, c) in seen or (r, c) in nonTraverse:
            return False

        if (r, c) == (ROW-1, COL-1):
            return True

        seen.add((r, c))
        res = travel(r+1, c) or travel(r-1, c) or travel(r, c-1) or \
            travel(r, c+1)

        seen.remove((r, c))
        return res

    def changeCol(r, c):
        while c >= 0 or grid[r][c] == ".":
            nonTraverse.add([r][c])
            c -= 1

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == "<":
                changeCol(r, c)
            elif grid[r][c] == "X":
                nonTraverse.add(r, c)
            elif grid[r][c] == "A":
                start[0], start[1] = r, c

    return travel(start[0], start[1])
    # print(grid)


print(
    isPossible(grid)
)
