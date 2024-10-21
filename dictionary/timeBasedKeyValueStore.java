/*
 * https://leetcode.com/problems/time-based-key-value-store/solution/
 set
 * Time: O(L*M)
 * Space: O(L*M)
 get
 * Time: O(N * timestamp *L)
 * Space: O(1)
 */
class TimeMap1 {

    Map<String, Map<Integer, String>> map;
    
    public TimeMap() {
        this.map = new HashMap<String, Map<Integer, String>>();
    }
    
    public void set(String key, String value, int timestamp) {
        this.map.putIfAbsent(key, new HashMap<Integer, String>());
        
        this.map.get(key).put(timestamp, value);
    }
    
    public String get(String key, int timestamp) {
        if(!this.map.containsKey(key)){
            return "";
        }
        
        for(int time = timestamp; time >= 1; time--){
            if(this.map.get(key).containsKey(time)){
                return this.map.get(key).get(time);
            }
        }
        
        return "";
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */

 /*
set(String key, String value, int timestamp):

Time Complexity: The putIfAbsent and put operations on a TreeMap both have a time complexity of (O(\log n)), where (n) is the number of timestamps for the given key.
Space Complexity: The space complexity is (O(n)) for storing the timestamps and their corresponding values in the TreeMap.
get(String key, int timestamp):

Time Complexity: The floorKey operation on a TreeMap has a time complexity of (O(\log n)), where (n) is the number of timestamps for the given key.
Space Complexity: The space complexity is (O(1)) as it only requires a constant amount of additional space for the floorKey operation.* 

  */
 class TimeMap {
    private Map<String, TreeMap<Integer, String>> map;

    public TimeMap() {
        this.map = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        this.map.putIfAbsent(key, new TreeMap<>());
        this.map.get(key).put(timestamp, value);
    }

    public String get(String key, int timestamp) {
        if (!this.map.containsKey(key)) {
            return "";
        }

        TreeMap<Integer, String> treeMap = this.map.get(key);
        Integer floorKey = treeMap.floorKey(timestamp);
        
        if (floorKey == null) {
            return "";
        }
        return treeMap.get(floorKey);
    }
}