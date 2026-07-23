# Last updated: 23/07/2026, 10:59:09
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        left, right = p.split("*")

        for i in range(len(s) + 1):
            if s.startswith(left, i):
                j = i + len(left)
                pos = s.find(right, j)
                if pos != -1:
                    return True

        return False