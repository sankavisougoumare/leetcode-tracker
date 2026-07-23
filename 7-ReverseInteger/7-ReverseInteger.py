# Last updated: 23/07/2026, 11:00:50
class Solution:
    def reverse(self, x):

        sign = -1 if x < 0 else 1
        x = abs(x)

        rev = 0

        while x:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        rev *= sign

        if rev < -2147483648 or rev > 2147483647:
            return 0

        return rev