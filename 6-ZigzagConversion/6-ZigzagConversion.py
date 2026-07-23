# Last updated: 23/07/2026, 11:00:52
class Solution:
    def convert(self, s, numRows):

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        current_row = 0
        direction = -1

        for char in s:
            rows[current_row] += char

            if current_row == 0 or current_row == numRows - 1:
                direction *= -1

            current_row += direction

        return "".join(rows)