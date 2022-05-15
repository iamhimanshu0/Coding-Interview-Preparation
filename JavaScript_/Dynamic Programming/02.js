/*
    Say that you are a traveler on a 2D grid. You begin the the
    top-left corner and your goal is to travel to the bottom-right
    corner. You may only move down or right.

    In how many ways can you travel to the gole on a grid
    with dimensions m*n? 
*/

// const gridTraveler = (m, n) => {
//   // base case
//   if (m == 1 && n == 1) return 1;
//   if (m == 0 || n == 0) return 0;
//   // going down + going right
//   return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);
// };

// console.log(gridTraveler(3, 3));
// console.log(gridTraveler(30, 1));
// console.log(gridTraveler(3, 2));
// console.log(gridTraveler(18, 18)); // taking long time / not returning

// using memoization
const gridTravelerMemo = (m, n, memo = {}) => {
  // base case
  const key = m + "," + n;
  if (key in memo) return memo[key];
  if (m == 1 && n == 1) return 1;
  if (m == 0 || n == 0) return 0;
  // going down + going right
  memo[key] =
    gridTravelerMemo(m - 1, n, memo) + gridTravelerMemo(m, n - 1, memo);
  return memo[key];
};

console.log(gridTravelerMemo(21, 21));


/*
    Memoization Recipe

    1. Make it work
    - visualize the problem as a tree
    - implement the tree using recursion
    - test it

    2. Make it efficient
    - add a memo object
    - add a base case to return memo values
    - store return values into the memo

*/