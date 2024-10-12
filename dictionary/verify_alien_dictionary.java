"""
https://leetcode.com/problems/verifying-an-alien-dictionary
Time: O(N * M)
Space: O(1)
"""
class Solution {
    int[] lookup = new int[26];
    public boolean isAlienSorted(String[] words, String order) {
        
        for(int index = 0; index < order.length(); index++){
            lookup[order.charAt(index)-'a'] = index;
        }
        
        for(int index = 1; index < words.length; ++index){            
            if(compare(words[index-1], words[index])){
                return false;  
            } 
        }
        
        return true;
    }
    
    private boolean compare(String prev, String current){
        int m = prev.length();
        int n = current.length();
        
        for(int index = 0; index < m && index < n; index++){
            if(prev.charAt(index) != current.charAt(index)){
                return lookup[prev.charAt(index)-'a'] > lookup[current.charAt(index)-'a'];    
            }
        }
        
        return m > n;
    }
}