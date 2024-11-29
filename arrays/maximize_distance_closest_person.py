from typing import List
"""
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        left = -1
        right = 0

        for index, value in enumerate(seats):
            if value == 1:
                left = index
            else:
                while right < len(seats) and (seats[right] == 0 or right < index):
                    right += 1

                left_distance = float('inf') if left == -1 else index - left
                right_distance = float('inf') if right == len(seats) or seats[right] == 0 else right - index

                max_distance = max(max_distance, min(left_distance, right_distance))

        return max_distance

    def maxDistToClosest1(self, seats):
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in xrange(N):
            if seats[i] == 1: left[i] = 0
            elif i > 0: left[i] = left[i-1] + 1

        for i in xrange(N-1, -1, -1):
            if seats[i] == 1: right[i] = 0
            elif i < N-1: right[i] = right[i+1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)