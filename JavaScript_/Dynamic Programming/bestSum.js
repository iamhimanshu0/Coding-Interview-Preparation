/*
    write a function that takes in a targetSum and an array of numbers as arguments.

    The function should return an array containing the shortest combination of numbers that add up to exactly the targetSum.

    If there is a tie for a shortest combination, you may return any one of the shortest

*/

// Brute force
// m - target sum, n = number length
// TC -> O(n^m * m)
// SC -> O(m*m) => O(m^2)
// const bestSum = (targetSum, numbers) => {
//   if (targetSum === 0) return [];
//   if (targetSum < 0) return null;

//   let shortestCombination = null;

//   for (let num of numbers) {
//     const remainder = targetSum - num;
//     remainderCombination = bestSum(remainder, numbers);
//     if (remainderCombination != null) {
//       const combination = [...remainderCombination, num];

//       //   if shorter
//       if (
//         shortestCombination === null ||
//         combination.length < shortestCombination.length
//       ) {
//         shortestCombination = combination;
//       }
//     }
//   }
//   return shortestCombination;
// };

// memo
// TC:-> O(m*n*m) => O(m^2*n)
// Sc :-> O(m^2)
const bestSum = (targetSum, numbers, memo = {}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return [];
  if (targetSum < 0) return null;

  let shortestCombination = null;

  for (let num of numbers) {
    const remainder = targetSum - num;
    remainderCombination = bestSum(remainder, numbers, memo);
    if (remainderCombination != null) {
      const combination = [...remainderCombination, num];

      //   if shorter
      if (
        shortestCombination === null ||
        combination.length < shortestCombination.length
      ) {
        shortestCombination = combination;
      }
    }
  }
  memo[targetSum] = shortestCombination;
  return memo[targetSum];
};

console.log(bestSum(7, [5, 3, 4, 7]));
console.log(bestSum(8, [2, 3, 5]));
console.log(bestSum(8, [1, 4, 5]));
console.log(bestSum(100, [1, 2, 5, 25]));
