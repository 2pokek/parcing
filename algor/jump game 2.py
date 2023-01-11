
def helper(i):
    if i == len(nums) - 1:
        return 0

    ans = float('inf')

    for j in range(1,nums[1]):
        ans = min(ans,1 +helper(i + j))
    return ans

