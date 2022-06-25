
class Backtrack:

    # Combination sum
    def combination_sum(self, candidates, target):
        output = []

        def backtrack(idx,arr, target):
            if idx == len(candidates):
                if target == 0:
                    output.append(arr[:])
                return
                
            if candidates[idx] <= target:
                arr.append(candidates[idx])
                backtrack(idx, arr, target- candidates[idx])
                arr.pop()

            backtrack(idx+1, arr, target)

        backtrack(0,[], target)
        return output

    def combination_sum_2(self, candidates, target):
        output = []

        def backtrack(idx, arr, target):
            if target == 0:
                output.append(arr[:])
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]: continue

                if candidates[i] > target: break

                arr.append(candidates[i])
                backtrack(i+1, arr, target - candidates[i])
                arr.pop()
        
        candidates.sort()
        backtrack(0,[], target)
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
        
        backtrack(0,[])
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
            if idx == len(nums) and nums[:] not in output:
                output.append(nums[:])
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                backtrack(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)
        return output


b = Backtrack()

print(
    # b.combination_sum_2([10,1,2,7,6,1,5],8)
    b.permutations_unique([1,1,2])
)