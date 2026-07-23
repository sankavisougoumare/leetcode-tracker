# Last updated: 23/07/2026, 11:00:54
class Solution:
    def longestPalindrome(self, s):
        if not s:
            return ""

        start, end = 0, 0

        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length of palindrome

        for i in range(len(s)):
            len1 = expandFromCenter(i, i)       # Odd length palindrome
            len2 = expandFromCenter(i, i + 1)   # Even length palindrome
            length = max(len1, len2)

            if length > end - start + 1:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]