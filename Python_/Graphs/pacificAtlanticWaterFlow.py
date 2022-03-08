"""
# https://leetcode.com/problems/pacific-atlantic-water-flow/

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights = [[1,2,2,3,5],
                  [3,2,3,4,4],
                  [2,4,5,3,1],
                  [6,7,1,4,5],
                  [5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Input: heights = [[2,1],
                  [1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
"""

def pacificAtlantic(matrix):
    # Check for an empty graph.
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    p_visited = set()
    a_visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j, visited):
        if (i, j) in visited:
            return
        visited.add((i, j))
        # Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                if matrix[next_i][next_j] >= matrix[i][j]:
                    traverse(next_i, next_j, visited)

    for row in range(rows):
        traverse(row, 0, p_visited)
        traverse(row, cols - 1, a_visited)

    for col in range(cols):
        traverse(0, col, p_visited)
        traverse(rows - 1, col, a_visited)

    return list(p_visited & a_visited)