"""
https://leetcode.com/problems/trapping-rain-water/editorial
"""
class Solution:
    # Time: O(n)
    # Space: O(1)
    def trap(self, height):
        left, right = 0, len(height) -1
        left_max, right_max = 0, 0
        units = 0

        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                units += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                units += right_max - height[right]
                right -=1

        return units

    def trap1(self, height):
        ans = 0
        size = len(height)
        for i in range(1, size - 1):
            left_max = 0
            right_max = 0
            # Search the left part for max bar size
            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])
            # Search the right part for max bar size
            for j in range(i, size):
                right_max = max(right_max, height[j])
            ans += min(left_max, right_max) - height[i]
        return ans