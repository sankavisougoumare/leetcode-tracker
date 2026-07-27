# Last updated: 27/07/2026, 14:56:04
1class Solution:
2    def minimumTotal(self, triangle):
3        # Start from the second-last row
4        for row in range(len(triangle) - 2, -1, -1):
5            for col in range(len(triangle[row])):
6                triangle[row][col] += min(
7                    triangle[row + 1][col],
8                    triangle[row + 1][col + 1]
9                )
10
11        return triangle[0][0]