/*
    The function should return an array containing any combination of elements that add up to exactly the targetSum.

    If there is no combination that adds up to the targetSum, then return null.

    If there are multiple combinations possible, you may return any single one.

*/
// m = targetSum
// n = numbers.length
// TC = O(n*m^2)
// SC = O(m^2)
const howSum = (targetSum, numbers) => {
  table = Array(targetSum + 1).fill(null);

  table[0] = [];

  for (let i = 0; i <= targetSum; i++) {
    if (table[i] != null) {
      for (let num of numbers) {
        table[i + num] = [...table[i], num];
      }
    }
  }
  return table[targetSum];
};

console.log(howSum(7, [5, 3, 4]));
