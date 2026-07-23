# Last updated: 23/07/2026, 10:59:03
class Solution:
    def maxDistance(self, moves: str) -> int:
        u=moves.count('U')
        d=moves.count('D')
        l=moves.count('L')
        r=moves.count('R')
        q=moves.count('_')
        return abs(r-l) + abs(u-d) +q
        