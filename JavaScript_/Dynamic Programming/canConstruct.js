/*

Write a function that accepts a target string and an array of strings.

the function should return a boolean indicating whether or not the 'target' can be constructed by concatenating elements of the 'wordBank' array.

you may reuse elements of 'wordBank' as many times as neeaded

*/

// Brute force
//               | = target.slice()
// TC => O(n^m * m)
// SC => O(m   * m)

// const canConstruct = (target, wordBank) => {
//   if (target === "") return true;

//   for (let word of wordBank) {
//     if (target.indexOf(word) === 0) {
//       const suffix = target.slice(word.length);
//       if (canConstruct(suffix, wordBank) === true) {
//         return true;
//       }
//     }
//   }
//   return false;
// };

// memo
// m = target.length, n = wordBank.length

//               | = target.slice()
// TC => O(n*m * m)
// SC => O(m   * m)

const canConstruct = (target, wordBank, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === "") return true;

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      if (canConstruct(suffix, wordBank, memo) === true) {
        memo[target] = true;
        return memo[target];
      }
    }
  }
  memo[target] = false;
  return memo[target];
};

console.log(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]));
console.log(
  canConstruct("skeatboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
);
console.log(canConstruct("himanshu", ["hi", "ma", "hu", "ns", "abcd"]));
console.log(
  canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e",
    "ee",
    "eee",
    "eeeee",
    "eeeeee",
  ])
);
