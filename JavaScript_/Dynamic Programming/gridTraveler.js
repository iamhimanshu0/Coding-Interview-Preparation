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
console.log(grid(30, 20));

// Tabulation Recipe
/*
  - visualize the problem as a table
  - size the table based on the inputs
  - initalize the table with default values
  - seed the trivial answer into the table
  - iterate through the table
  - fill further positions based on the      current position
*/
