console.log("Dynamic Programming");

// Memoization
// Tabulation

/*
    fibonacci Sequence

    1,1,2,3,5,8,13,21,34,....
*/

// const Classicalfib = (n) => {
//   if (n <= 2) return 1;
//   return fib(n - 1) + fib(n - 2);
// };

// console.log(Classicalfib(6));
// console.log(Classicalfib(7));
// console.log(Classicalfib(80)); // not going to work

// memoization
// keys will be args to fn, value will be the return value

const memoFib = (n, memo = {}) => {
  // return value if alredy in memo
  if (n in memo) return memo[n];
  if (n <= 2) return 1;
  //   if not then add value in memo
  memo[n] = memoFib(n - 1, memo) + memoFib(n - 2, memo);
  return memo[n];
};

console.log(memoFib(50));
console.log(memoFib(135));
console.log(memoFib(55));
console.log(memoFib(51));
