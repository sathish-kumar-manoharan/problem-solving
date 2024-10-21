/*
 * https://leetcode.com/problems/first-missing-positive
 * 
 */
class Solution {

    /*
    Time complexity: O(n)
    Space complexity: O(1)
    */

    public int firstMissingPositive(int[] nums) {
        int n = nums.length;

        // Use cycle sort to place positive elements smaller than n
        // at the correct index
        int i = 0;
        
        while (i < n) {
            int correctIdx = nums[i] - 1;
            
            if (nums[i] > 0 && nums[i] <= n && nums[i] != nums[correctIdx]) {
                swap(nums, i, correctIdx);
            } else {
                i++;
            }
        }

        // Iterate through nums
        // return smallest missing positive integer
        for (i = 0; i < n; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }

        // If all elements are at the correct index
        // the smallest missing positive number is n + 1
        return n + 1;
    }

    // Swaps two elements in nums
    private void swap(int[] nums, int index1, int index2) {
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
    }

    /*
    Time complexity: O(n)
    Space complexity: O(n)
     */
    public int firstMissingPositive1(int[] nums) {
        int n = nums.length;
        boolean[] seen = new boolean[n + 1]; // Array for lookup

        // Mark the elements from nums in the lookup array
        for (int num : nums) {
            if (num > 0 && num <= n) {
                seen[num] = true;
            }
        }

        // Iterate through integers 1 to n
        // return smallest missing positive integer
        for (int i = 1; i <= n; i++) {
            if (!seen[i]) {
                return i;
            }
        }

        // If seen contains all elements 1 to n
        // the smallest missing positive number is n + 1
        return n + 1;
    }
}