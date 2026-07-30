class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.right = self.tail
        self.tail.left = self.head

    def isEmpty(self) -> bool:
        return self.head.right == self.tail
        
    def append(self, value: int) -> None:
        # Setup Previous Ptr
        previousPtr = self.tail.left

        # Create Node with it's connections
        newNode = Node(value, previousPtr, self.tail)

        # Update ptrs for prev and tail ptrs
        self.tail.left = newNode
        previousPtr.right = newNode

    def appendleft(self, value: int) -> None:
        # Setup next Ptr
        nextPtr = self.head.right

        # Create Node with it's connections
        newNode = Node(value, self.head, nextPtr)

        # Update ptrs for prev and tail ptrs
        self.head.right = newNode
        nextPtr.left = newNode
        

    def pop(self) -> int:
        if self.isEmpty():
            return - 1

        removePtr = self.tail.left
        prevPtr = removePtr.left
        prevPtr.right = self.tail
        self.tail.left = prevPtr

        return removePtr.value


    def popleft(self) -> int:
        if self.isEmpty():
            return - 1

        removePtr = self.head.right
        nextPtr = removePtr.right
        self.head.right = nextPtr
        nextPtr.left = self.head

        return removePtr.value
