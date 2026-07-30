class ListNode:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1, None)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        # Setting up loop
        count = 0
        currPtr = self.head.next

        # While ptr exists, advance through list
        # until it is exhausted or until we reach the index
        while currPtr:
            if count == index:
                return currPtr.val
            currPtr = currPtr.next
            count += 1

        return -1
        
    def insertHead(self, val: int) -> None:
        newHead = ListNode(val, self.head.next)
        self.head.next = newHead
        if self.tail == self.head:
            self.tail = newHead

        print(f"Inserting Head-value {val}: {self.getValues()}")
        

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        print(f"Inserting Tail-value {val}: {self.getValues()}")

    def remove(self, index: int) -> bool:
        currPtr = self.head
        count = 0

        while currPtr.next:
            if count == index:
                
                if currPtr.next == self.tail:
                    self.tail = currPtr
                    currPtr.next = None

                else:
                    currPtr.next = currPtr.next.next
                print(f"Removed value at place {count}: {self.getValues()}")
                return True
            currPtr = currPtr.next
            count += 1
        print(f"Value not found {currPtr.val}: {self.getValues()}")
        return False


    def getValues(self) -> List[int]:
        res = []

        currPtr = self.head.next
        while currPtr:
            res.append(currPtr.val)
            currPtr = currPtr.next

        return res
        
