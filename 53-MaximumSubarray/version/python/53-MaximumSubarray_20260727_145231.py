# Last updated: 27/07/2026, 14:52:31
1class Solution:
2    def maxSubArray(self, nums):
3        current_sum = max_sum = nums[0]
4
5        for i in range(1, len(nums)):
6            current_sum = max(nums[i], current_sum + nums[i])
7            max_sum = max(max_sum, current_sum)
8
9        return max_sum