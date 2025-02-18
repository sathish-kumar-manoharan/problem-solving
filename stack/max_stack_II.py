"""
https://leetcode.com/problems/max-stack/
You must come up with a solution that supports O(1) for each top call and O(logn) for each other call.
"""
from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.stack = SortedList()
        self.values = SortedList()
        self.count = 0

    def push(self, x: int) -> None:
        self.stack.add((self.count, x))
        self.values.add((x, self.count))

        self.count += 1

    def pop(self) -> int:
        index, value = self.stack.pop()
        self.values.remove((value, index))

        return value

    def top(self) -> int:
        return self.stack[-1][1]

    def peekMax(self) -> int:
        return self.values[-1][0]

    def popMax(self) -> int:
        value, index = self.values.pop()
        self.stack.remove((index, value))

        return value


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()