/*
    Write a function that accepts a target string and an array of strings.
    
    The function should return 1 2D array containing all of the ways that the target can be constructed by concatenating elements of the wordBank array. Each element of the 2D array should represent one combination that constructs the target

*/

// m = target.length, n = wordBank.length

// Brute force
//               | = target.slice()
// TC => O(n^m)
// SC => O(m)  -> height of recurssion tree

const allConstruct = (target, wordBank, memo = {}) => {
  if (target in memo) return memo[target];
  if (target === "") return [[]];

  const result = [];

  for (let word of wordBank) {
    if (target.indexOf(word) === 0) {
      const suffix = target.slice(word.length);
      const suffixWays = allConstruct(suffix, wordBank, memo);
      const targetWays = suffixWays.map((way) => [word, ...way]);
      result.push(...targetWays);
    }
  }
  memo[target] = result;
  return result;
};

console.log(allConstruct("hello", ["cat", "dog", "mouse"]));
console.log(
  allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
);

// this is just a simple comment
