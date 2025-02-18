class MaxStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        
        current_max = self.stack[-1][1]
        
        self.stack.append((val, max(current_max, val)))

    def pop(self) -> None:       
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]

    def getMax(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()