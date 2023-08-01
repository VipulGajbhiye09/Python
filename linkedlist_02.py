## Circular Linked List

class CircularLinkedList:
    def createList(self):
        self.root=self.last=None

    def insert_left(self,data):
        n=Node(data)#Node Creation
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            n.next=self.root#1
            self.root=n#2
            self.last.next=self.root#3
        print(data,"inserted")
