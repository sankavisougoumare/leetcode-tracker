# Last updated: 27/07/2026, 15:08:20
1class Solution:
2    def maxProduct(self, nums):
3        first = 0
4        second = 0
5
6        for num in nums:
7            if num > first:
8                second = first
9                first = num
10            elif num > second:
11                second = num
12
13        return (first - 1) * (second - 1)