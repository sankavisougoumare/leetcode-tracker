# Last updated: 27/07/2026, 15:09:16
1class Solution:
2    def isSubsequence(self, s: str, t: str) -> bool:
3        i = 0  # pointer for s
4
5        for char in t:
6            if i < len(s) and s[i] == char:
7                i += 1
8
9        return i == len(s)