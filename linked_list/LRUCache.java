
package com.practice.LinkedList;

class LRUCache1 {
    int capacity;
    Map<Integer, ListNode> dic;
    ListNode head;
    ListNode tail;
    
    public LRUCache1(int capacity) {
        this.capacity = capacity;

        dic = new HashMap<>();
        head = new ListNode(-1, -1);
        tail = new ListNode(-1, -1);

        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        if (!dic.containsKey(key)) {
            return -1;
        }
        
        ListNode node = dic.get(key);

        this.remove(node);
        this.add(node);

        return node.val;
    }
    
    public void put(int key, int value) {
        if (dic.containsKey(key)) {
            this.remove(dic.get(key));
        }
        
        ListNode node = new ListNode(key, value);
        dic.put(key, node);

        this.add(node);
        
        if (dic.size() > capacity) {
            ListNode nodeToDelete = head.next;

            this.remove(nodeToDelete);
            dic.remove(nodeToDelete.key);
        }
    }
    
    public void add(ListNode node) {
        ListNode previousEnd = tail.prev;
        previousEnd.next = node;
        node.prev = previousEnd;
        node.next = tail;
        tail.prev = node;
    }
    
    public void remove(ListNode node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
}

class LRUCache {
    int capacity;
    LinkedHashMap<Integer, Integer> dic;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        dic = new LinkedHashMap<>(capacity, 0.75f, true) { // true is passed for last accessed order and false is for insertion order
            @Override
            protected boolean removeEldestEntry(Map.Entry<Integer, Integer> eldest) {
                return size() > capacity;
            }
        };
    }
    
    public int get(int key) {
        return dic.getOrDefault(key, -1);
    }
    
    public void put(int key, int value) {
        dic.put(key, value);
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */