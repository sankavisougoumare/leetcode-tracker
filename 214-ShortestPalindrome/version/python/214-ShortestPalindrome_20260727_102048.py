# Last updated: 27/07/2026, 10:20:48
1class Solution:
2    def shortestPalindrome(self, s: str) -> str:
3        rev = s[::-1]
4        temp = s + "#" + rev
5
6        lps = [0] * len(temp)
7
8        j = 0
9        for i in range(1, len(temp)):
10            while j > 0 and temp[i] != temp[j]:
11                j = lps[j - 1]
12
13            if temp[i] == temp[j]:
14                j += 1
15                lps[i] = j
16
17        pal_len = lps[-1]
18
19        return rev[:len(s) - pal_len] + s