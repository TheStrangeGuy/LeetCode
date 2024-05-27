'''
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1] 

        def binary_search(low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    first = mid
                    last = mid
                    while first > low and nums[first - 1] == target:
                        first -= 1
                    while last < high and nums[last + 1] == target:
                        last += 1
                    return [first, last]
            return [-1, -1]
        return binary_search(0, len(nums) - 1)