'''
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
'''

class Solution(object):
    def combinationSum(self, candidates, target):
        results = []
        def backtrack(start, remaining, curr_list):
            if remaining == 0:
                results.append(curr_list[:])
                return
            if remaining < 0:
                return
            for i in range(start, len(candidates)):
                curr_list.append(candidates[i])
                backtrack(i, remaining - candidates[i], curr_list)  
                curr_list.pop()  
        backtrack(0, target, [])
        return results