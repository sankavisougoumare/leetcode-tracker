# Last updated: 27/07/2026, 14:49:09
1class Solution:
2    def maxArea(self, height):
3        left, right = 0, len(height) - 1
4        max_area = 0
5
6        while left < right:
7            h = min(height[left], height[right])
8            width = right - left
9            max_area = max(max_area, h * width)
10
11            if height[left] < height[right]:
12                left += 1
13            else:
14                right -= 1
15
16        return max_area