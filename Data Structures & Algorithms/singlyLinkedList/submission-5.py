class ListNode:
    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        currPtr = self.head.next
        count = 0
        while currPtr != None:
            if count == index:
                return currPtr.val

            else:
                currPtr = currPtr.next
                count += 1

        return -1

    def insertHead(self, val: int) -> None:
        # No Head
        # Create a node, set head = to it
        if self.head.next == None:
            self.head.next = ListNode(val)
            self.tail = self.head.next

        # 
        else:
            newHead = ListNode(val, self.head.next)
            self.head.next = newHead

    def insertTail(self, val: int) -> None:
        if self.head.next == None:
            self.head.next = ListNode(val)
            self.tail = self.head.next

        else:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next

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
                return True
            currPtr = currPtr.next
            count += 1

        return False

    def getValues(self) -> List[int]:
        res = []
        currPtr = self.head.next
        while currPtr:
            res.append(currPtr.val)
            currPtr = currPtr.next
        return res

        
