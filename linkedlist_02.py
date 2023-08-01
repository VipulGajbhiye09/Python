## Circular Linked List

class CircularLinkedList:
    def createList(self):
        self.root=self.last=None

    def insert_left(self,data):
        n=Node(data)   #Node Creation
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            n.next=self.root  #1
            self.root=n  #2
            self.last.next=self.root#3
        print(data,"inserted")
        
    def delete_left(self):
        if self.root==None:
            print("List Empty")
        else:
            t=self.root  #1
            if self.root==self.last:  #one element
                self.root=self.last=None
            else:
                self.root=self.root.next  #2
                self.last.next=self.root  #3
            print(t.data,"deleted")
            
    def insert_right(self,data):
        n=Node(data)  #Node Creation
        if self.root==None:
            self.root=self.last=n
            self.last.next=self.root
        else:
            self.last.next=n  #1
            self.last=n  #2
            self.last.next=self.root  #3
        print(data,"inserted")
