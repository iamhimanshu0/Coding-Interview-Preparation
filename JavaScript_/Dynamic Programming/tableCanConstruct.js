/*
    The function should return a boolean indicating wheather or not the 'target' can be constructed by concatenating elements of the 'wordBank' array.

    You may reuse elements of 'wordBank' as many times as needed.
*/
// m = target,
// n = wordBank.length
//
// TC => O(n*m * m) => O(m^2*n)
// SC => O(m)

const canConstruct = (target, wordBank) => {
  const table = Array(target.length + 1).fill(false);

  table[0] = true;

  for (let i = 0; i <= target.length; i++) {
    if (table[i] === true) {
      for (let word of wordBank) {
        // if word matches the characters starting with position i
        if (target.slice(i, i + word.length) === word) {
          table[i + word.length] = true;
        }
      }
    }
  }
  return table[target.length];
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
