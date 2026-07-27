# Last updated: 27/07/2026, 14:53:41
1class Solution:
2    def threeSum(self, nums):
3        nums.sort()
4        result = []
5        n = len(nums)
6
7        for i in range(n - 2):
8            # Skip duplicate first elements
9            if i > 0 and nums[i] == nums[i - 1]:
10                continue
11
12            left = i + 1
13            right = n - 1
14
15            while left < right:
16                total = nums[i] + nums[left] + nums[right]
17
18                if total == 0:
19                    result.append([nums[i], nums[left], nums[right]])
20
21                    # Skip duplicates
22                    while left < right and nums[left] == nums[left + 1]:
23                        left += 1
24                    while left < right and nums[right] == nums[right - 1]:
25                        right -= 1
26
27                    left += 1
28                    right -= 1
29
30                elif total < 0:
31                    left += 1
32                else:
33                    right -= 1
34
35        return result