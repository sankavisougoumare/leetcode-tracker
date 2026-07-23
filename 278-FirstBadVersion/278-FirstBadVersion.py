# Last updated: 23/07/2026, 10:59:21
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid   # first bad could be here
            else:
                left = mid + 1  # move to right
        
        return left