class Solution:
    def jump(self, nums: List[int]) -> int:
        @lru_cache(None)
        def helper(i):
            if i >= len(nums) - 1:
                return 0

            ans = float('inf')

            for j in range(1,nums[1]+1):
                ans = min(ans,1 +helper(i + j))
            return ans
        return helper(0)

