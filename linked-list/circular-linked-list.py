class Node: 
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node()


    def __str__(self):
        current = self.head.next
        string = ""
        while current:
            string += str(current.val) + " -> "
            current = current.next
        string += "None"
        return string

    # GET
    # Time: O(n)
    # Space: O(1)
    def get(self, index:int) -> int:
        if index >= self.size:
            return -1
        
        current = self.head
        for _ in range(index + 1):
            current = current.next

        return current.val
    
    # ADD AT INDEX, IF INDEX IS INVALID: ADD HEAD OR DO NOTHING
    # Time: O(n)
    # Space: O(1)
    def addAt(self, index:int, val:int) -> None:
        if index > self.size: # invalid index
            return
        
        if index < 0:
            index = 0
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        newNode = Node(val, prev.next)
        newNode.next = prev.next
        prev.next = newNode

        self.size += 1

    # ADD AT HEAD
    # Time: O(1)
    # Space: O(1)
    def addAtHead(self, val:int) -> None:
        self.addAt(0, val)


    # DELETE AT INDEX, IF INDEX IS INVALID: DO NOTHING
    # Time: O(n)
    # Space: O(1)
    def deleteAt(self, index:int) -> None:
        if index >= self.size or index < 0:
            return
        
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        prev.next = prev.next.next
        self.size -= 1

    # DELETE AT TAIL
    # Time: O(n)
    # Space: O(1)
    def deleteAtTail(self) -> None:
        self.deleteAt(self.size - 1)

#################################################