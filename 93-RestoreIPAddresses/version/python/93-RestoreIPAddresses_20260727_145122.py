# Last updated: 27/07/2026, 14:51:22
1class Solution:
2    def restoreIpAddresses(self, s: str):
3        res = []
4
5        def backtrack(index, path):
6            
7            if len(path) == 4:
8                if index == len(s):
9                    res.append(".".join(path))
10                return
11
12            for length in range(1, 4):
13                if index + length > len(s):
14                    break
15
16                part = s[index:index + length]
17
18                if len(part) > 1 and part[0] == '0':
19                    continue
20
21                if int(part) <= 255:
22                    path.append(part)
23                    backtrack(index + length, path)
24                    path.pop()  
25
26        backtrack(0, [])
27        return res