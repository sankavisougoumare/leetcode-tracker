# Last updated: 23/07/2026, 10:59:01
class Solution:
    def maxSum(self,nums,k,mul):
        nums.sort(reverse=True)
        total=0
        for i in range(k):
            if mul>1:
                total+=nums[i]*mul
            else:
                total+=nums[i]
            mul-=1
        return total
        