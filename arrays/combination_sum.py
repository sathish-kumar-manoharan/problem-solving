from typing import List

""""
https://leetcode.com/problems/combination-sum-ii
Time: O(N^(T/M))
Space: O(T/M)

"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remain, path, start):
            if remain < 0:
                return

            if remain == 0:
                result.append(path[:])
                return

            for index in range(start, len(candidates)):
                path.append(candidates[index])
                backtrack(remain - candidates[index], path, index)
                path.pop()

        backtrack(target, [], 0)
              
        return result

