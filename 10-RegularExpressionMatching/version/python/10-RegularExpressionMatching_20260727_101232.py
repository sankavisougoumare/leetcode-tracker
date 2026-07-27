# Last updated: 27/07/2026, 10:12:32
1from functools import lru_cache
2
3class Solution:
4    def isMatch(self, s: str, p: str) -> bool:
5
6        @lru_cache(None)
7        def dp(i, j):
8            if j == len(p):
9                return i == len(s)
10
11            first_match = (
12                i < len(s) and
13                (s[i] == p[j] or p[j] == '.')
14            )
15
16            if j + 1 < len(p) and p[j + 1] == '*':
17                return dp(i, j + 2) or (first_match and dp(i + 1, j))
18            else:
19                return first_match and dp(i + 1, j + 1)
20
21        return dp(0, 0)