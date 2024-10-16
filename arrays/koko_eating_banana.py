import math
from typing import List


class Solution:
    """
    Time: O(N*M)
    Space: O(1)
    """
    def minEatingSpeed1(self, piles: List[int], h: int) -> int:
        #Start at an eating speed of 1.
        speed = 1

        while True:
            hour_spent = 0

            for pile in piles:
                hour_spent += math.ceil(pile / speed)    

            # Check if Koko can finish all the piles within h hours,
            # If so, return speed. Otherwise, let speed increment by
            # 1 and repeat the previous iteration.                
            if hour_spent <= h:
                return speed
            else:
                speed += 1

        """
        Time: O(N * log(M))
        Space: O(1)
        """
        def minEatingSpeed(self, piles: List[int], h: int) -> int:
            left = 1
            right = max(piles)
            
            while left < right:
                middle = (left + right) // 2            
                hour_spent = 0
                
                for pile in piles:
                    hour_spent += math.ceil(pile / middle)
                
                # Check if middle is a workable speed, and cut the search space by half.
                if hour_spent <= h:
                    right = middle
                else:
                    left = middle + 1
            
            # Once the left and right boundaries coincide, we find the target value,
            # that is, the minimum workable eating speed.
            return left