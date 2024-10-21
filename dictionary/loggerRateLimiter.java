/*
 * https://leetcode.com/problems/logger-rate-limiter/
 * Time: O(1)
 * Space:O(N)
 */
class Logger {
    Map<String, Integer> lookup;

    public Logger() {
        this.lookup = new HashMap<>();
    }
    
    public boolean shouldPrintMessage(int timestamp, String message) {
        if(!this.lookup.containsKey(message) || (timestamp - this.lookup.get(message)) >= 10){
            this.lookup.put(message, timestamp);
            return true;
        }
        
        return false;
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * boolean param_1 = obj.shouldPrintMessage(timestamp,message);
 */