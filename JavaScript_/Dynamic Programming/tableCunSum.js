/*
    write a function that takes in a targetSum and an array of numbers as arguments.

    The function should return a boolean indicating whether
    or not it is possible to generate the tragetSum using number
    from the array.

    You may use an element of the array as many times as needed.
    You may assume that all input numbers are nonegative.
*/

// m = targetSum
// n = numbers.length
// TC = O(nm)
// SC = O(m)

const canSum = (targetSum, numbers) => {
  const table = Array(targetSum + 1).fill(false);
  table[0] = true;

  for (let i = 0; i <= targetSum; i++) {
    if (table[i] === true) {
      //   look ahead (if true)
      for (let num of numbers) {
        table[i + num] = true;
      }
    }
  }
  return table[targetSum];
};

console.log(canSum(7, [5, 3, 4, 7]));
