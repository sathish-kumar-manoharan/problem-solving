from linked_list.ListNode import ListNode

class MaxStack:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.lookup = {}

    def push(self, val: int) -> None:
        to_be_pushed = ListNode(val)

        if val not in self.lookup:
            self.lookup[val] = [(to_be_pushed, to_be_pushed.value)]
        else:
            self.lookup[val].append((to_be_pushed, to_be_pushed.value))
            
        self.add(to_be_pushed)

    def add(self, node: ListNode) -> None:
        if not node:
            return
        
        prev_end = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev_end
        prev_end.next = node

    def pop(self) -> int:       
        to_be_removed = self.tail.prev

        self.remove(to_be_removed)

        if self.lookup[to_be_removed.value]:
            self.lookup[to_be_removed.value].pop()
        else:
            del self.lookup[to_be_removed.value]

        return to_be_removed.value
    
    def remove(self, node: ListNode) -> None:
        if not node:
            return
        
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
  
    def top(self) -> int:
        return self.tail.prev.value

    def peekMax(self) -> int:
        last_value = self.tail.prev.value

        _, max_value = self.lookup[last_value][-1]

        return max_value

    def popMax(self) -> int:
        max_value = self.peekMax()
        max_value_node = self.lookup[max_value].pop()

        if not self.lookup[max_value]:
            del self.lookup[max_value]
        
        self.remove(max_value_node)

        return max_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()