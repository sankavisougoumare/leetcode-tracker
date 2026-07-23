# Last updated: 23/07/2026, 11:00:20
class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        left = 1
        right = x

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                ans = mid
                left = mid + 1

            else:
                right = mid - 1

        return ans