"""
https://leetcode.com/problems/meeting-rooms-ii
Time: O(N log N)
Space: O(N)
"""
class Solution {
    public int minMeetingRooms(int[][] intervals) {
        Arrays.sort(intervals, (a, b)->(a[0] - b[0]));
        
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) -> a[1] - b[1]);
        
        for(int[] interval: intervals){
            if(!pq.isEmpty() && pq.peek()[1] <= interval[0]){
                pq.poll();
            }
            
            pq.offer(interval);
        }
        
        return pq.size();
    }
}