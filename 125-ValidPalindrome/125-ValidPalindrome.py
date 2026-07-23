# Last updated: 23/07/2026, 10:59:54
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]