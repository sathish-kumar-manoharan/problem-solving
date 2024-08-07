from typing import Counter, List

"""
Intuition
We don't care the value of A[i],
we care if A[i] % mod == k.

So if A[i] % mod == k,
we take A[i] as 1,
otherwise 0.


Explanation
we calculate the prefix sum acc of A,
then acc mean the number of A[i] % mod == k in i + 1 first elements.

count is a hashmap,
where count[v] means the number of prefix array that have acc % mod == k.
and we initial count[0] = 1 for empty prefix subarray.

Then we iterate a in A,
and we update prefix sum acc,
and update increment res by count[(acc - k) % mod].

Finally return res


Complexity
Time O(n)
Space O(mod)
https://leetcode.com/problems/count-of-interesting-subarrays/

"""
class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        res = acc = 0
        count = Counter({0: 1})
        for num in nums:
            acc = (acc + (1 if num % mod == k else 0)) % mod
            res += count[(acc - k) % mod]
            count[acc] += 1
        return res