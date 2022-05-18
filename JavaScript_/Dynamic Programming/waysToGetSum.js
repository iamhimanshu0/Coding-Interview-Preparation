/*
Given 3 numbers {1, 3, 5}, we need to tell
the total number of ways we can form a number 'N' 
using the sum of the given three numbers.
*/

// brute force
// const getSum = (number) => {
//   if (number < 0) return 0;
//   if (number == 0) return 1;

//   return getSum(number - 1) + getSum(number - 3) + getSum(number - 5);
// };

// memo
const getSum = (number, memo = {}) => {
  if (number in memo) return memo[number];
  if (number < 0) return 0;
  if (number == 0) return 1;

  memo[number] = getSum(number - 1) + getSum(number - 3) + getSum(number - 5);
  return memo[number];
};

console.log(getSum(40));
