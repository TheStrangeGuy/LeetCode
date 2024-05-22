'''
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
'''

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        sol = set()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  
                    continue
                l, r = j + 1, len(nums) - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        sol.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1  
                    elif total < target:
                        l += 1
                    else:
                        r -= 1
        return list(sol)
