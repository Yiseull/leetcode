class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * size
        dp[0] = nums[0]

        for i in range(1, size):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[size - 1]