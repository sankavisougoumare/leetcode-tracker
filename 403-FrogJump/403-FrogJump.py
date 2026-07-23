# Last updated: 23/07/2026, 10:59:18
class Solution:
    def canCross(self, stones):
        stone_set = set(stones)
        last = stones[-1]

        # map: stone position -> set of possible jump sizes reaching it
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        for stone in stones:
            for jump in dp[stone]:
                for next_jump in (jump - 1, jump, jump + 1):
                    if next_jump > 0:
                        next_pos = stone + next_jump
                        if next_pos in stone_set:
                            dp[next_pos].add(next_jump)

        return len(dp[last]) > 0