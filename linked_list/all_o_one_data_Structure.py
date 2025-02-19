"""
https://leetcode.com/problems/all-oone-data-structure/
Time: O(1)
Space: O(N)
"""
class Node:
    def __init__(self, freq):
        self.keys = set()
        self.freq = freq
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup = {}


    def inc(self, key: str) -> None:
        if key in self.lookup:
            node = self.lookup[key]

            freq = node.freq

            node.keys.remove(key)

            next_node = node.next

            if next_node == self.tail or next_node.freq != freq + 1:
                new_node = Node(freq + 1)
                new_node.keys.add(key)
                new_node.prev = node
                new_node.next = next_node

                node.next = new_node
                next_node.prev = new_node

                self.lookup[key] = new_node
            else:
                next_node.keys.add(key)
                self.lookup[key] = next_node
            
            # Remove the current node if it has no keys left
            if not node.keys:
                self.removeNode(node)
        else:
            first_node = self.head.next

            if first_node == self.tail or first_node.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = first_node
                self.head.next = newNode
                first_node.prev = newNode
                self.lookup[key] = newNode
            else:
                first_node.keys.add(key)
                self.lookup[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.lookup:
            return  # Key does not exist

        node = self.lookup[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # Remove the key from the map if freq is 1
            del self.lookup[key]
        else:
            prevNode = node.prev
            if prevNode == self.head or prevNode.freq != freq - 1:
                # Create a new node if the previous node does not exist or freq is not freq - 1
                newNode = Node(freq - 1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.lookup[key] = newNode
            else:
                # Decrement the existing previous node
                prevNode.keys.add(key)
                self.lookup[key] = prevNode

        # Remove the node if it has no keys left
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""

        return next(iter(self.tail.prev.keys)) if len(self.tail.prev.keys) > 0 else ""

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""

        return next(iter(self.head.next.keys)) if len(self.head.next.keys) > 0 else ""
        
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode  # Link previous node to next node
        nextNode.prev = prevNode  # Link next node to previous node

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()