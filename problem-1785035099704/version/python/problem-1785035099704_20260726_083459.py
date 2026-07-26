# Last updated: 26/07/2026, 08:34:59
1class Solution:
2    def largestInteger(self, n: int, s: int) -> int:
3        if s==0:
4            return 0
5        if s>9 * n:
6            return -1
7        ans =[]
8        for _ in range(n):
9            digit =min(9,s)
10            ans.append(str(digit))
11            s -= digit
12        return int("".join(map(str,ans)))
13        