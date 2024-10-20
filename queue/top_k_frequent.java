class Solution {
    /**
     * using heap, that has
     * time : O(N logN)
     * space: O(N + K)
     */
    public int[] topKFrequent1(int[] nums, int k) {       
        if(nums == null || nums.length == k){
            return nums;
        }
        
        Map<Integer,Integer> lookup = new HashMap<>();
        
        for(int num: nums){
            lookup.put(num, lookup.getOrDefault(num, 0) + 1);
        }
               
        Queue<Integer> heap = new PriorityQueue<>((i1, i2)-> lookup.get(i1) - lookup.get(i2));
        
        for(int num : lookup.keySet()){
            heap.offer(num);
            
            if(heap.size() > k){
                heap.poll();
            }
        }
        
        
        int[] result = new int[k];
        
        for(int index = 0; index < k; index++){
            result[index] = heap.poll();
        }
        
        return result;
    }

        /**
     * using heap, that has
     * time : O(N)
     * space: O(N + K)
     */
    public int[] topKFrequent(int[] nums, int k) {       
        if(nums == null || nums.length == k){
            return nums;
        }
        
        Map<Integer,Integer> lookup = new HashMap<>();
        
        for(int num: nums){
            lookup.put(num, lookup.getOrDefault(num, 0) + 1);
        }
               
        List<List<Integer>> bucket = new ArrayList<>(nums.length + 1);

        for (int i = 0; i <= nums.length; i++) {
            bucket.add(new ArrayList<>());
        }
        
        for(int key : lookup.keySet()){
             int freq = lookup.get(key);
            
            if(freq < bucket.size()){
                bucket.get(freq).add(key);    
            }
        }
               
        List<Integer> topFreq = new ArrayList<>();
        
        for(int index = bucket.size()-1; index >= 0 ; index--){
            topFreq.addAll(bucket.get(index));
        }
        
        int[] result = new int[k];
        
        for(int index = 0; index < k; index++){
            if(index < topFreq.size()){
                result[index] = topFreq.get(index);
            }
        }
        
        return result;
    }
}