/*
    write a function that takes in a targetSum and an array
    of numbers as arguments.

    The function should return a boolean indicating whether
    or not it is possible to generate the tragetSum using number
    from the array.

    You may use an element of the array as many times as needed.
    You may assume that all input numbers are nonegative.
*/
// TC => o(n^m) : m = target , n = array len
// SC => 0(m)

const canSumFirst = (target, number) => {
  // base case
  if (target === 0) return true;
  if (target < 0) return false;

  for (let num of number) {
    const remainder = target - num;
    if (canSumFirst(remainder, number) === true) {
      return true;
    }
  }
  return false;
};

// console.log(canSumFirst(7, [2, 3]));
// console.log(canSumFirst(7, [5, 3, 4, 7]));
// console.log(canSumFirst(7, [2, 4]));
// console.log(canSumFirst(300, [7, 14])); // this one is not going to work(takes a long time to run)

// memotization
// TC => o(m*n)
// SC => 0(m)
const canSumMemo = (target, number, memo = {}) => {
  if (target in memo) return memo[target];
  // base case
  if (target === 0) return true;
  if (target < 0) return false;

  for (let num of number) {
    const remainder = target - num;
    if (canSumMemo(remainder, number, memo) === true) {
      memo[target] = true;
      return true;
    }
  }
  memo[target] = false;
  return false;
};

console.log(canSumMemo(300, [7, 14]));
