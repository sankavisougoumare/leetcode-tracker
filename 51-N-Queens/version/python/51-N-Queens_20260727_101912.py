# Last updated: 27/07/2026, 10:19:12
1from typing import List
2
3class Solution:
4    def solveNQueens(self, n: int) -> List[List[str]]:
5        res = []
6
7        board = [["."] * n for _ in range(n)]
8
9        cols = set()
10        diag1 = set()   # row - col
11        diag2 = set()   # row + col
12
13        def backtrack(row):
14            if row == n:
15                res.append(["".join(r) for r in board])
16                return
17
18            for col in range(n):
19                if (col in cols or
20                    row - col in diag1 or
21                    row + col in diag2):
22                    continue
23
24                board[row][col] = "Q"
25                cols.add(col)
26                diag1.add(row - col)
27                diag2.add(row + col)
28
29                backtrack(row + 1)
30
31                board[row][col] = "."
32                cols.remove(col)
33                diag1.remove(row - col)
34                diag2.remove(row + col)
35
36        backtrack(0)
37        return res