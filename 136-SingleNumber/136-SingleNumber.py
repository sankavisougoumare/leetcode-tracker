# Last updated: 23/07/2026, 10:59:52
class Solution:
    def singleNumber(self, nums):
        result = 0

        for num in nums:
            result ^= num

        return result