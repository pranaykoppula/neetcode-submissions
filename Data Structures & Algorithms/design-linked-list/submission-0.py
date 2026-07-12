class ListNode:
    def __init__(self,val=0):
        self.val=val
        self.prev=None
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newHead = ListNode(val=val)
        if not self.head:
            self.head = self.tail = newHead
        else:
            newHead.next = self.head
            self.head.prev = newHead
            self.head = newHead
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newTail = ListNode(val=val)
        if not self.tail:
            self.head = self.tail = newTail
        else:
            self.tail.next = newTail
            newTail.prev = self.tail
            self.tail = newTail
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index <= 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            temp = ListNode(val=val)
            temp.prev = curr.prev
            temp.next = curr
            curr.prev.next = temp
            curr.prev = temp
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.head: self.head.prev = None
            else: self.tail = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            if self.tail: self.tail.next = None
            else: self.head = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1