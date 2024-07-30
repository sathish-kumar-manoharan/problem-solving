class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self) -> str:
        return f"->'{self.value}'"