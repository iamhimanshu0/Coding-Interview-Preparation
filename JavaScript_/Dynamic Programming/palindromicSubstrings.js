const countSubstrings = (s) => {
  let count = 0;
  let matrix = [];

  for (let char of s) {
    matrix.push(Array(s.length).fill(0));
  }

  for (let i = 0; i < s.length; i++) {
    matrix[i][i] = 1;
    count++;
  }

  for (let col = 1; col < s.length; col++) {
    for (let row = 0; row < col; row++) {
      // this check palindrom for string length <=2
      if (row === col - 1 && s[col] === s[row]) {
        matrix[row][col] = 1;
        count++;
      }
      // this checks for string length 3 or more and inner string palindrom
      else if (matrix[row + 1][col - 1] === 1 && s[col] === s[row]) {
        matrix[row][col] = 1;
        count++;
      }
    }
  }
  return count;
};

console.log(countSubstrings("aaa"));
