class ListNode:
    
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class LinkedList:
    
    def __init__(self):
        self.headPtr = ListNode(-1)
        self.tailPtr = self.headPtr

    def get(self, index: int) -> int:
        count = 0
        currPtr = self.headPtr.next

        while currPtr:
            if count == index:
                return currPtr.val

            currPtr = currPtr.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        newHead = ListNode(val, self.headPtr.next)

        if self.headPtr.next == None:
            self.tailPtr = newHead
        self.headPtr.next = newHead

    def insertTail(self, val: int) -> None:
        self.tailPtr.next = ListNode(val)
        self.tailPtr = self.tailPtr.next
        if self.headPtr.next == None:
            self.headPtr.next = self.tailPtr 

    def remove(self, index: int) -> bool:
        currPtr = self.headPtr
        count = 0
        while currPtr.next:
            if index == count:
                if currPtr.next == self.tailPtr:
                    self.tailPtr = currPtr
                    currPtr.next = None
                else:
                    currPtr.next = currPtr.next.next
                return True

            currPtr = currPtr.next
            count += 1

        return False

            
    def getValues(self) -> List[int]:
        res = []
        currPtr = self.headPtr.next
        while currPtr:
            res.append(currPtr.val)
            currPtr = currPtr.next
        return res
        
