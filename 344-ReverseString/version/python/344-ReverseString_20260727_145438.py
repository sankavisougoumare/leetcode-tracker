# Last updated: 27/07/2026, 14:54:38
1class Solution:
2    def reverseString(self, s):
3        left = 0
4        right = len(s) - 1
5
6        while left < right:
7            s[left], s[right] = s[right], s[left]
8            left += 1
9            right -= 1