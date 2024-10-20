from typing import List
/*
https://leetcode.com/problems/merge-intervals/
Time: O(n log n)
Space: O(log N)
*/
class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0){
            return new int[0][0];
        }
        
        Arrays.sort(intervals, (i1, i2) -> i1[0] - i2[0]);
        
        LinkedList<int[]> merged = new LinkedList<>();
        
        for (int[] interval: intervals){
            if(merged.isEmpty() || merged.getLast()[1] < interval[0]){
                merged.add(interval);
            }else{
                merged.getLast()[1] = Math.max(interval[1], merged.getLast()[1]);
            }
        }
        
        return merged.toArray(new int[merged.size()][]);
    }
}