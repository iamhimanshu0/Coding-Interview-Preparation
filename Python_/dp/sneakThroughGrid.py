grid = [
    [".", ".", "<", "."],
    ["X", "A", ".", "X"],
    [".", "<", ".", "."],
    ["X", ".", "X", "."],
]


def isPossible(grid):
    ROW, COL = len(grid), len(grid[0])
    seen = set()

    def travel(r, c):
        if r < 0 or c < 0 or r >= ROW or c >= COL or ((r, c)) in seen or grid[r][c] != ".":
            return
        seen.add((r, c))
        travel(r+1, c),
        travel(r-1, c),
        travel(r, c-1),
        travel(r, c+1)

    def changeCol(r, c):
        while c >= 0:
            grid[r][c] == "X"
            c -= 1

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == "<":
                changeCol(r, c)
            elif grid[r][c] == "A":
                if travel(r, c):
                    return True

    print(grid)


print(
    isPossible(grid)
)
