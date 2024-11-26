from typing import List

""""
https://leetcode.com/problems/combination-sum-ii
Time: O(2^N)
Space: O(N)

"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # Sort the candidates to facilitate duplicate skipping and efficient pruning
        candidates.sort()

        self.backtrack(candidates, target, 0, [], result)
              
        return result

    def backtrack(self, candidates, target, start, path, result):
        if target < 0:
            return

        if target == 0:
            result.append(path)
            return

        for index in range(start, len(candidates)):
            # To prevent same number is considered for duplicate combination
            if index > start and candidates[index] == candidates[index-1]:
                continue

            self.backtrack(
                candidates,
                target - candidates[index],
                index + 1,
                path + [candidates[index]],
                result)