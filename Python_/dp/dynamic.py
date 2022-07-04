# memoization (top down)
# | Tabulation (button up)
# | Space Optimization

class DynamicProgramming:

    def fibonacii(self, n):

        # top down (memoization)
        # TC -> o(n), SC -> o(n)
        def find(n, dp):
            if n <= 1:
                return n

            if dp[n] != 0:
                return dp[n]

            dp[n] = find(n-1, dp) + find(n-2, dp)
            return dp[n]

        # tabulation (buttom-up)
        # TC -> o(n), SC -> o(n)
        def find2(n, dp):
            for i in range(2, n+1):
                dp[i] = dp[i-1] + dp[i-2]

            return dp[n]

        # space optimization
        # TC -> o(n), SC -> o(1)
        def find3(n):
            prev2 = 0
            prev = 1
            for i in range(2, n+1):
                cur1 = prev2 + prev

                prev2 = prev
                prev = cur1

            return prev

        dp = [0 for _ in range(n+1)]
        dp[1] = 1

        # return find2(n, dp)
        return find3(n)

    def climbing_stairs(self, n):

        def find1(n, memo={}):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n

            memo[n] = find1(n-1, memo) + find1(n-2, memo)
            return memo[n]

        return find1(n+1)


dp = DynamicProgramming()

print(
    # dp.fibonacii(15)
    dp.climbing_stairs(3)
)
