/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 * https://leetcode.com/problems/binary-tree-maximum-path-sum
 * Time: O(N)
 * Space: O(N)
 */
class Solution {
    int maxSum = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) {
     
        this.maxPathSumRecursive(root);
        
        return this.maxSum;
    }
    
    private int maxPathSumRecursive(TreeNode node){
        
        if(node == null){
            return 0;
        }
        
        int leftMax = Math.max(maxPathSumRecursive(node.left), 0);
        int rightMax = Math.max(maxPathSumRecursive(node.right), 0);
        
        this.maxSum = Math.max(this.maxSum, leftMax + rightMax + node.val);
        
        return Math.max(leftMax, rightMax) + node.val;
    }
}