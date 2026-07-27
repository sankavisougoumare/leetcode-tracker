# Last updated: 27/07/2026, 15:12:31
1class Solution:
2    def maxAscendingSum(self, nums):
3        current_sum = nums[0]
4        max_sum = nums[0]
5
6        for i in range(1, len(nums)):
7            if nums[i] > nums[i - 1]:
8                current_sum += nums[i]
9            else:
10                current_sum = nums[i]
11
12            max_sum = max(max_sum, current_sum)
13
14        return max_sum