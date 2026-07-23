# Last updated: 23/07/2026, 11:00:32
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0 
        
        i = 0  
        for j in range(1, len(nums)):  
            if nums[j] != nums[i]:  
                i += 1  
                nums[i] = nums[j]  
        
        return i + 1  


solution = Solution()
nums1 = [1,1,2]
k1 = solution.removeDuplicates(nums1)
print(k1, nums1[:k1])  # Output: 2, [1,2]

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = solution.removeDuplicates(nums2)
print(k2, nums2[:k2])  
