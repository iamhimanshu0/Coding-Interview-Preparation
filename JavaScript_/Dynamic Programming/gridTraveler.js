/*
    say that you are a traveler on a 2D grid, you begin in the top-left corner and your goal is to travel to the bottom-right corner. you may only move down or right.

    In how many ways you travel to the goal on a grid with m*n grid 

*/
// TC:- O(mn)
// SC:- O(mn)
const grid = (m, n) => {
  const table = Array(m + 1)
    .fill()
    .map(() => Array(n + 1).fill(0));
  table[1][1] = 1;

  for (let i = 0; i <= m; i++) {
    for (let j = 0; j <= n; j++) {
      const current = table[i][j];
      if (j + 1 <= n) table[i][j + 1] += current;
      if (i + 1 <= m) table[i + 1][j] += current;
    }
  }
  return table[m][n];
};

console.log(grid(3, 2));
