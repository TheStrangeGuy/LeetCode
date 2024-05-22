'''
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            l, r = i + 1, len(nums) - 1  
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                diff = abs(total - target)
                if diff == 0:
                    return total
                if abs(diff) < abs(closest_sum - target):
                    closest_sum = total
                elif total < target:
                    l += 1  
                elif total > target:
                    r -= 1 
        return closest_sum       