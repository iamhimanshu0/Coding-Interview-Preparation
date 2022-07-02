
class Backtrack:

    # Combination sum
    def combination_sum(self, candidates, target):
        output = []

        def backtrack(idx, arr, target):
            if idx == len(candidates):
                if target == 0:
                    output.append(arr[:])
                return

            if candidates[idx] <= target:
                arr.append(candidates[idx])
                backtrack(idx, arr, target - candidates[idx])
                arr.pop()

            backtrack(idx+1, arr, target)

        backtrack(0, [], target)
        return output

    def combination_sum_2(self, candidates, target):
        output = []

        def backtrack(idx, arr, target):
            if target == 0:
                output.append(arr[:])
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                if candidates[i] > target:
                    break

                arr.append(candidates[i])
                backtrack(i+1, arr, target - candidates[i])
                arr.pop()

        candidates.sort()
        backtrack(0, [], target)
        return output

    def subset(self, nums):
        output = []

        def backtrack(idx, arr):
            # if idx == len(nums):
            output.append(arr[:])
            # return

            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i+1, arr)
                arr.pop()

            # arr.append(nums[idx])
            # backtrack(idx+1, arr)
            # arr.pop()

            # backtrack(idx+1, arr)

        backtrack(0, [])
        return output

    def subsets_With_Dup(self, nums):
        def backtrack(start, end, tmp):
            ans.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                backtrack(i+1, end, tmp)
                tmp.pop()
        ans = []
        nums.sort()
        backtrack(0, len(nums), [])
        return ans

    def permutations(self, nums):
        output = []

        def backtrack(idx):
            if idx == len(nums):
                output.append(nums[:])
                return

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)
        return output

    def permutations_unique(self, nums):
        output = []

        def backtrack(idx):
            if idx == len(nums):
                output.append(nums[:])
                return

            lookup = set()

            for i in range(idx, len(nums)):
                if nums[i] not in lookup:
                    nums[idx], nums[i] = nums[i], nums[idx]
                    backtrack(idx+1)
                    nums[idx], nums[i] = nums[i], nums[idx]
                    lookup.add(nums[i])

        backtrack(0)
        return output

    def pallindrome_partitioning(self, s):
        output = []

        def isPallindrome(st):
            return st == st[::-1]

        def backtrack(idx, arr):
            if idx == len(s)+1:
                output.append(arr[:])
                return

            for i in range(idx, len(s)+1):
                if isPallindrome(s[idx-1:i]):
                    arr.append(s[idx-1:i])
                    backtrack(i+1, arr)
                    arr.pop()

        backtrack(1, [])
        return output

    def next_permutation(self, nums):
        i = j = len(nums)-1

        # check to see if giving number is increasing or not
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:  # numbers are in descending order
            nums.reverse()
            return nums

        k = i-1  # find the last "ascending" position
        print(k)

        while nums[j] <= nums[k]:
            j -= 1
        # print(j,k)
        nums[k], nums[j] = nums[j], nums[k]

        l, r = k+1, len(nums)-1  # reverse the second part

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums

    def n_queens(self, n):

        col = set()

        posDig = set()

        negDig = set()

        board = [["."]*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in col or (r+c) in posDig or (r-c) in negDig:
                    continue

                col.add(c)
                posDig.add(r+c)
                negDig.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                col.remove(c)
                posDig.remove(r+c)
                negDig.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return res

    def letter_combinations_of_phone_number(self, digits):

        buttons = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def backtrack(idx, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return

            for c in buttons[digits[idx]]:
                backtrack(idx+1, curStr+c)

        if digits:
            backtrack(0, "")

        return res

    def word_search(self, board, word):
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r, c) in path):
                return False
            path.add((r, c))

            res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1)
                   or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False


b = Backtrack()

print(
    # b.combination_sum_2([10,1,2,7,6,1,5],8)
    # b.pallindrome_partitioning(list("aab"))
    # b.permutations()
    # b.next_permutation([1,2,3])
    # b.n_queens(4),
    # b.letter_combinations_of_phone_number("234")
    b.word_search(board=[["C", "A", "A"],
                         ["A", "A", "A"],
                         ["B", "C", "D"]],

                  word="AAB")
)
