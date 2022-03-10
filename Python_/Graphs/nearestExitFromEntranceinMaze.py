"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

"""


maze = [["+","+",".","+"],
        [".",".",".","+"],
        ["+","+","+","."]]
entrance = [1,2]

def nearestExit(maze, entrance):
    ex, ey = entrance
    r, c = len(maze), len(maze[0])

    def onBorder(i,j):
        if (i in [0, r-1] or j in [0, c-1]) and (i,j) != (ex, ey):
            return True
        return False

    def isnotWall(i,j):
        if 0<=i<r and 0<=j<c and maze[i][j] == ".":
            return True
        else:
            return False

    maze[ex][ey] = "+"
    queue = [(ex, ey,0)]
    while queue:
        i, j , steps = queue.pop(0)
        if onBorder(i,j):
            return steps
        
        for r1, c1 in [(0,1),(0,-1),(1,0),(-1,0)]:
            if isnotWall(r1+i, c1+j):
                maze[r1+i][c1+j] = "+"
                queue.append((r1+i, c1+j, steps+1))

    return -1

print(nearestExit(maze, entrance))