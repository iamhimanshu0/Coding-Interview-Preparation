/*
Write a function that accepts a target string and an array of strings.

The function should return the number of ways that the 'target' can be construted by concatenating elements of the 'wordBank' array

You can resue elements of 'wordBank' as many time as needed.

*/

const countConstruct = (target, wordBank, memo = {}) => {
  if (target === "") return 1;
  if (target in memo) return memo[target];
  let totalCount = 0;

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const numWays = countConstruct(target.slice(word.length), wordBank, memo);

      totalCount += numWays;
    }
  }
  memo[target] = totalCount;
  return totalCount;
};

console.log(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(
  countConstruct("skeatboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
);
console.log(countConstruct("himanshu", ["hi", "ma", "hu", "ns", "abcd"]));
console.log(
  countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeee", [
    "e",
    "ee",
    "eee",
    "eeeee",
    "eeeeee",
  ])
);
