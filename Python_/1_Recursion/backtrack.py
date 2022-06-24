
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
            # if idx == len(candidates):
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

b = Backtrack()
print(
    b.combination_sum_2([10,1,2,7,6,1,5],8)
)