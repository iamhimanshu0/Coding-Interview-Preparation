/*
    Write a function that takes in a targetSum and an array
    of number as arguments.

    The function should return an array containing any combination
    of elements that add up to exactly the targetSum. If there is no
    combination that add up to the targetSum, else retur null

    If there are multiple combinations possiable, you may return any
    single one.

*/

// TC => o(n^m * m) : m = target , n = array len
// SC => 0(m)
// const howSum = (targetSum, numbers) => {
//   if (targetSum === 0) return [];
//   if (targetSum < 0) return null;

//   for (let num of numbers) {
//     const remainder = targetSum - num;
//     const remainderResult = howSum(remainder, numbers);

//     if (remainderResult != null) {
//       return [...remainderResult, num];
//     }
//   }
//   return null;
// };

// memo
// Tc => O(n*m^2)
// SC => O(m*m) => O(m^2)

const howSum = (targetSum, numbers, memo = {}) => {
  if (targetSum in memo) return memo[targetSum];
  if (targetSum === 0) return [];
  if (targetSum < 0) return null;

  for (let num of numbers) {
    const remainder = targetSum - num;
    const remainderResult = howSum(remainder, numbers, memo);

    if (remainderResult != null) {
      memo[targetSum] = [...remainderResult, num];
      return [...remainderResult, num];
    }
  }
  memo[targetSum] = null;
  return null;
};

console.log(howSum(7, [2, 3]));
console.log(howSum(7, [5, 3, 4, 7]));
console.log(howSum(7, [2, 4]));
console.log(howSum(8, [2, 3, 5]));
console.log(howSum(300, [20, 50, 100]));
