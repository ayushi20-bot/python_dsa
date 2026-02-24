class Node:
    def __init__(self, value=None):
        self.data = value
        self.next = None

class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != self.head):
                t1 = t1.next
            t1.next = temp
            temp.next = self.head
        else:
            self.head = temp
            temp.next = self.head  

    def insertAtBeg(self,value):
        temp = Node(value)
        
        if(self.head == None):
            self.head = temp
            temp.next = self.head  
        
        else:
            t1 = self.head

            while t1.next != self.head:
                t1 = t1.next

            temp.next = self.head
            t1.next = temp
            self.head = temp
     
    def insertInMid(self,value,x):
        temp = Node(value)
        t1 = self.head

        while(t1.next != self.head):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next
    
    def deleteCLL(self, value):
        if self.head is None:
            return

        curr = self.head
        prev = None

        # Case: Only one node
        if curr.next == self.head:
            if curr.data == value:
                self.head = None
            return

        # Case: Deleting head
        if curr.data == value:
            last = self.head
            while last.next != self.head:
                last = last.next

            last.next = self.head.next
            self.head = self.head.next
            return

        # Case: Deleting non-head
        prev = curr
        curr = curr.next

        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def printLL(self):
        t1 = self.head
        while(t1.next != self.head):
            print(t1.data)
            t1 =t1.next
        print(t1.data)

obj = CircularLinkedList()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtBeg(5)
obj.insertInMid(15, 10)
obj.deleteCLL(15)
obj.printLL()