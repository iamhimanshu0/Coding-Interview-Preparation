/*
    write a function that takes in a number as an argument, the function should return the n-th number of the Fibonacci sequence.

    The 0th number of the sequence is 0
    The 1th number of the sequence is 1

*/

// TC :- O(N)
// SC :- O(N)
const tabluationFib = (n) => {
  let dp = Array(n + 1).fill(0);
  dp[1] = 1;
  for (let i = 2; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2];
  }

  return dp[n];
};

console.log(tabluationFib(5));
console.log(tabluationFib(7));
console.log(tabluationFib(8));
console.log(tabluationFib(50));
