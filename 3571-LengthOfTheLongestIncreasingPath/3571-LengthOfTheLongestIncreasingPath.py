# Last updated: 23/07/2026, 10:59:11
from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates, k):
        x0, y0 = coordinates[k]

        arr = []
        for x, y in coordinates:
            if (x < x0 and y < y0) or (x > x0 and y > y0):
                arr.append((x, -y))

        arr.sort()

        lis = []
        for _, y in arr:
            y = -y
            pos = bisect_left(lis, y)
            if pos == len(lis):
                lis.append(y)
            else:
                lis[pos] = y

        return len(lis) + 1